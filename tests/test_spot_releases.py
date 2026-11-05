from pathlib import Path
import tempfile
import zipfile
import pytest
from scripts import spot_releases as sr


def make_zip(path: Path, members: dict[str, bytes]):
    with zipfile.ZipFile(path, 'w') as z:
        for n, b in members.items():
            z.writestr(n, b)


def test_reject_traversal_and_absolute_paths():
    for name in ('../outside', '/tmp/danger', 'foo/../../x', 'a\\b'):
        with pytest.raises(ValueError):
            sr.reject_extra(name)


def test_app_needs_complete_sources_and_pinned_public_key(tmp_path):
    file = tmp_path/'app.zip'
    make_zip(file, {'VERSION': b'0.31.1\n', 'SPOT_v27.py': b'', 'spot_update.py': b''})
    with pytest.raises(ValueError, match='Vertrauensanker'):
        sr.validate_zip(file,'app')


def test_os_needs_package_manifest(tmp_path):
    file = tmp_path/'os.zip'
    make_zip(file, {'spot_os/VERSION':b'0.1.7\n','spot_os/setup_entry.py':b''})
    with pytest.raises(ValueError, match='Installationsdateien'):
        sr.validate_zip(file,'os')


def test_download_without_all_four_assets_must_fail(tmp_path):
    (tmp_path/'app').mkdir()
    with pytest.raises(ValueError, match='fehlt'):
        sr.verify_release('app',tmp_path/'app')


def test_pins_are_64_hex_bytes_and_reference_keys_exist():
    for kind, cfg in sr.SNAPSHOT.items():
        assert len(cfg['archive_sha256'])==64
        assert len(cfg['key_sha256'])==64
        assert sr.sha256((sr.ROOT/cfg['key']).read_bytes())==cfg['key_sha256']
        assert cfg['archive'].endswith('.zip')


def test_complete_synthetic_ed25519_app_release(monkeypatch, tmp_path):
    """Never contacts GitHub. Exercises manifest + trust + checksum + ZIP end to end."""
    import hashlib
    import json
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives.serialization import Encoding,PublicFormat

    private=Ed25519PrivateKey.generate()
    public=private.public_key().public_bytes(Encoding.PEM,PublicFormat.SubjectPublicKeyInfo)
    root=tmp_path/'guide';root.mkdir()
    (root/'keys').mkdir()
    (root/'keys/spot-app.pub').write_bytes(public)
    monkeypatch.setattr(sr,'ROOT',root)
    spec=dict(sr.SNAPSHOT['app'])
    filename=spec['archive']
    release=tmp_path/'release';release.mkdir()
    make_zip(release/filename,{
        'VERSION':b'0.31.1\n','SPOT_v27.py':b'print("hello")\n',
        'spot_update.py':b'# verified fixture\n',
        'assets/trust/spot-release.pub':public,
    })
    spec['key_sha256']=hashlib.sha256(public).hexdigest()
    spec['archive_sha256']=hashlib.sha256((release/filename).read_bytes()).hexdigest()
    spec['archive_size']=(release/filename).stat().st_size
    monkeypatch.setitem(sr.SNAPSHOT,'app',spec)
    meta=dict(schema=1,kind='app',version='0.31.1',channel='stable',
              platform='raspios-debian13-aarch64',repository=spec['repository'],
              asset=filename,size=spec['archive_size'],sha256=spec['archive_sha256'])
    data=json.dumps(meta,sort_keys=True).encode()
    (release/'update.json').write_bytes(data)
    (release/'update.json.sig').write_bytes(private.sign(data))
    (release/'SHA256SUMS.txt').write_text(''.join(
        hashlib.sha256((release/n).read_bytes()).hexdigest()+'  '+n+'\n'
        for n in (filename,'update.json','update.json.sig')))
    assert sr.verify_release('app',release)['signature']=='valid'
    (release/filename).write_bytes((release/filename).read_bytes()+b'bad')
    with pytest.raises(ValueError,match='ZIP-Hash'):
        sr.verify_release('app',release)
