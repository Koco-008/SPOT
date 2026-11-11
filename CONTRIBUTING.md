# Contributing to SPOT

Issues and pull requests for hardware improvements, documentation fixes, and reproducible software problems are welcome.

## Issues

Describe the problem, the steps to reproduce it, and the expected result. For hardware-related issues, include the component model/revision, wiring or assembly step, and SPOT App / SPOT OS versions where relevant.

Do not include passwords, private keys, tokens, or personal information in logs or screenshots.

## Pull requests

- Keep changes focused and describe what they fix or improve.
- Update the relevant BOM, assembly instructions, or technical documentation when hardware files change.
- Include test results or clear reproduction steps for software-related changes.
- Do not include third-party files unless their redistribution terms permit it.

Run the repository checks before submitting:

```bash
python -m pytest tests -q
```
