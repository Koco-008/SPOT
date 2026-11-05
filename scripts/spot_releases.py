#!/usr/bin/env python3
"""Pinned download, Ed25519 verification and safe extraction of SPOT BMA releases.

Only for the frozen BMA snapshot (App 0.31.1 / OS 0.1.7). This script never
installs or executes downloaded code, changes the OS, or uses GitHub tokens.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import urllib.request
from urllib.parse import urlparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MAX_DOWNLOAD = 40 * 1024 * 1024
MAX_EXTRACT_TOTAL = 90 * 1024 * 1024
ALLOW_HOSTS = {"github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com"}

SNAPSHOT = {
    "app": {
        "repository": "Koco-008/SPOT-Releases", "tag": "v0.31.1", "version": "0.31.1",
        "archive": "spot-0.31.1.zip", "manifest": "update.json", "signature": "update.json.sig",
        "key": "keys/spot-app.pub", "key_sha256": "be3ddaf4363b0c9257a3a171b7cbac05789d05a27f6a9898b1869a9f76b20827",
        "archive_sha256": "14c96dadd591bb9878607035eb71d52a607bc1f4cb0f6d6a01032bba249df6fc",
        "archive_size": 585122,
    },
    "os": {
        "repository": "Koco-008/SPOT-OS-Releases", "tag": "os-v0.1.7", "version": "0.1.7",
        "archive": "spot-os-0.1.7.zip", "manifest": "os-update.json", "signature": "os-update.json.sig",
        "key": "keys/spot-os.pub", "key_sha256": "b142b246c22fd6f56f4207b86bbd5dcef09b122d228af81c0c51130d4309f907",
        "archive_sha256": "4d5b7bc6a41d88c440caa300f130c4fc0409605893e6a8167b7e8ac71181b8b0",
        "archive_size": 1680416,
    },
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reject_extra(name: str) -> None:
    p = PurePosixPath(name)
    if (not name or '\\' in name or ':' in name or name != str(p) or p.is_absolute()
            or '..' in p.parts or any(part in ('', '.') for part in p.parts)):
        raise ValueError('Unsicherer Archivpfad: ' + name)


def validate_zip(path: Path, which: str) -> dict[str, str]:
    seen = set()
    entries = {}
    with zipfile.ZipFile(path) as archive:
        info = archive.infolist()
        if not info or len(info) > 600:
            raise ValueError('Unplausible Anzahl ZIP-Einträge')
        total = 0
        for member in info:
            name = member.filename
            reject_extra(name)
            if name in seen or member.is_dir():
                raise ValueError('Doppelter oder unzulässiger ZIP-Eintrag: ' + name)
            seen.add(name)
            mode = member.external_attr >> 16
            if stat.S_IFMT(mode) not in (stat.S_IFREG, 0):
                raise ValueError('Symbolischer Link / Spezialdatei im ZIP: ' + name)
            if member.flag_bits & 1:
                raise ValueError('Verschlüsselter ZIP-Eintrag: ' + name)
            total += member.file_size
            if member.file_size > 10 * 1024 * 1024 or total > MAX_EXTRACT_TOTAL:
                raise ValueError('Unplausible Archivgrösse')
            raw = archive.read(member)
            if len(raw) != member.file_size:
                raise ValueError('Verkürzter ZIP-Eintrag: ' + name)
            entries[name] = sha256(raw)
        if which == 'app':
            if 'SPOT_v27.py' not in entries or 'spot_update.py' not in entries or 'VERSION' not in entries:
                raise ValueError('App-Archiv enthält nicht alle erforderlichen Dateien')
            if archive.read('VERSION').decode().strip() != SNAPSHOT['app']['version']:
                raise ValueError('App-VERSION stimmt nicht')
            if 'assets/trust/spot-release.pub' not in entries:
                raise ValueError('Vertrauensanker fehlt im App-Paket')
            if sha256(archive.read('assets/trust/spot-release.pub')) != SNAPSHOT['app']['key_sha256']:
                raise ValueError('Abweichender App-Vertrauensanker im Paket')
        else:
            meta = 'spot_os/PACKAGE.json'
            if meta not in entries or 'spot_os/VERSION' not in entries or 'spot_os/setup_entry.py' not in entries:
                raise ValueError('OS-Installationsdateien fehlen')
            internal = strict_json(archive.read(meta))
            if (internal.get('schema') != 1 or internal.get('kind') != 'os-installer'
                    or internal.get('version') != SNAPSHOT['os']['version']):
                raise ValueError('Falsches internes OS-Paketmanifest')
            expected = internal.get('files')
            if not isinstance(expected, dict) or set(expected) != set(entries) - {meta}:
                raise ValueError('Falscher interner OS-Dateisatz')
            for name, hashval in expected.items():
                if entries[name] != hashval:
                    raise ValueError('Unstimmige innere OS-Dateiprüfsumme: '+name)
            if archive.read('spot_os/VERSION').decode().strip() != SNAPSHOT['os']['version']:
                raise ValueError('OS-VERSION stimmt nicht')
            if 'spot_os/trust/spot-os-release.pub' not in entries or sha256(
                archive.read('spot_os/trust/spot-os-release.pub')) != SNAPSHOT['os']['key_sha256']:
                raise ValueError('Abweichender OS-Vertrauensanker im Paket')
    return entries


def strict_json(raw: bytes):
    def pairs(items):
        d = {}
        for k, v in items:
            if k in d:
                raise ValueError('Doppelte JSON-Schlüssel: ' + k)
            d[k] = v
        return d
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Ungültige JSON-Konstante')))


def verify_release(which: str, directory: Path) -> dict:
    spec = SNAPSHOT[which]
    directory = Path(directory)
    names = (spec['archive'], spec['manifest'], spec['signature'], 'SHA256SUMS.txt')
    raws = {}
    for name in names:
        path = directory/name
        if not path.is_file() or path.is_symlink() or path.stat().st_size > MAX_DOWNLOAD:
            raise ValueError('Release-Datei fehlt oder ist ungültig: '+str(path))
        raws[name] = path.read_bytes()
    key = (ROOT/spec['key']).read_bytes()
    if sha256(key) != spec['key_sha256']:
        raise ValueError('Unabhängig gepinnter öffentlicher Schlüssel wurde verändert')
    try:
        from cryptography.hazmat.primitives.serialization import load_pem_public_key
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    except ImportError as exc:
        raise RuntimeError('Python cryptography fehlt (z. B. sudo apt install python3-cryptography)') from exc
    pub = load_pem_public_key(key)
    if not isinstance(pub, Ed25519PublicKey):
        raise ValueError('Kein Ed25519-Public-Key')
    try:
        pub.verify(raws[spec['signature']], raws[spec['manifest']])
    except Exception as exc:
        raise ValueError('Ed25519-Signatur ungültig: Download nicht vertrauenswürdig') from exc
    manifest = strict_json(raws[spec['manifest']])
    if not isinstance(manifest, dict):
        raise ValueError('Release-Manifest muss ein JSON-Objekt sein')
    common = (manifest.get('version') == spec['version'] and
              manifest.get('repository') == spec['repository'] and
              manifest.get('asset') == spec['archive'] and
              manifest.get('channel') == 'stable' and
              manifest.get('platform') == 'raspios-debian13-aarch64' and
              type(manifest.get('size')) is int and manifest.get('size') == spec['archive_size'] and
              manifest.get('sha256') == spec['archive_sha256'])
    if not common:
        raise ValueError('Signiertes Manifest passt nicht zum eingefrorenen BMA-Stand')
    if which == 'app':
        if manifest.get('kind') != 'app' or manifest.get('schema') != 1:
            raise ValueError('Falscher App-Manifesttyp')
    else:
        if (manifest.get('kind') != 'spot-os' or manifest.get('schema') != 1
                or manifest.get('tag') != spec['tag'] or manifest.get('sequence') != 107
                or manifest.get('requires_os_min') != '0.1.6' or manifest.get('requires_os_max') != '0.1.6'
                or manifest.get('reboot') is not False):
            raise ValueError('Falscher OS-Manifesttyp/Sequenz/Upgradevertrag')
    if len(raws[spec['archive']]) != spec['archive_size'] or sha256(raws[spec['archive']]) != spec['archive_sha256']:
        raise ValueError('ZIP-Hash / signierte Grösse stimmen nicht')
    checksums = {}
    for row in raws['SHA256SUMS.txt'].decode('ascii').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})\s+([^\s]+)', row)
        if not match or match.group(2) in checksums:
            raise ValueError('Ungültige oder doppelte SHA256SUMS-Zeile')
        checksums[match.group(2)] = match.group(1)
    expected = {n:sha256(raws[n]) for n in names[:-1]}
    if checksums != expected:
        raise ValueError('SHA256SUMS stimmt nicht mit dem Download überein')
    entries = validate_zip(directory/spec['archive'],which)
    return {'part':which,'version':spec['version'],'channel':'stable',
            'signature':'valid', 'zip_sha256':spec['archive_sha256'], 'files':len(entries)}


class RestrictedRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        u = urlparse(newurl)
        if u.scheme != 'https' or u.hostname not in ALLOW_HOSTS or u.username or u.password or u.port not in (None, 443):
            raise ValueError('Unerwartete GitHub-Downloadumleitung')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_asset(spec: dict, name: str, directory: Path) -> None:
    url = f"https://github.com/{spec['repository']}/releases/download/{spec['tag']}/{name}"
    opener = urllib.request.build_opener(RestrictedRedirect(), urllib.request.ProxyHandler({}))
    request = urllib.request.Request(url, headers={'User-Agent':'SPOT-BMA-Build-Guide/1'})
    with opener.open(request, timeout=65) as response:
        content = response.read(MAX_DOWNLOAD+1)
    if not content or len(content) > MAX_DOWNLOAD:
        raise ValueError('Unplausible Downloadgrösse: '+name)
    path = directory/name
    temporary = directory/(name+'.download')
    with temporary.open('xb') as target:
        target.write(content)
        target.flush()
        os.fsync(target.fileno())
    os.replace(temporary,path)


def fetch_release(which: str, base: Path) -> dict:
    spec = SNAPSHOT[which]
    folder = base/which
    folder.mkdir(parents=True,exist_ok=True)
    for name in (spec['archive'],spec['manifest'],spec['signature'],'SHA256SUMS.txt'):
        if (folder/name).exists():
            raise FileExistsError('Vorhandene Release-Datei nicht überschreiben: '+str(folder/name))
        print(f'Lade {which}: {name}',flush=True)
        fetch_asset(spec,name,folder)
    return verify_release(which,folder)


def extract_verified(which: str, folder: Path, output: Path) -> dict:
    result=verify_release(which,folder)
    if output.exists():
        raise FileExistsError('Zielordner muss neu sein: '+str(output))
    output.mkdir(parents=True,mode=0o700)
    archive=folder/SNAPSHOT[which]['archive']
    with zipfile.ZipFile(archive) as z:
        for entry in z.infolist():
            target=output.joinpath(*PurePosixPath(entry.filename).parts)
            target.parent.mkdir(parents=True,exist_ok=True)
            with target.open('xb') as file:
                file.write(z.read(entry))
    return result


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('fetch','verify','extract'))
    parser.add_argument('--part',choices=('all','app','os'),default='all')
    parser.add_argument('--directory',type=Path,default=Path('downloads'))
    parser.add_argument('--output',type=Path,help='New extraction directory (extract only)')
    args=parser.parse_args(argv)
    if args.action=='extract' and (args.part=='all' or args.output is None):
        parser.error('extract benötigt --part app|os und --output NEUER_ORDNER')
    for which in ('app','os') if args.part=='all' else (args.part,):
        if args.action=='fetch':result=fetch_release(which,args.directory)
        elif args.action=='verify':result=verify_release(which,args.directory/which)
        else:result=extract_verified(which,args.directory/which,args.output)
        print(json.dumps(result,sort_keys=True,ensure_ascii=False),flush=True)


if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        print('FEHLER: '+str(exc),file=sys.stderr)
        sys.exit(1)
