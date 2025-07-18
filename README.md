# Passly

A simple, open-source CLI toolkit for auditing and cleaning exported password manager data.

![Test Status](https://img.shields.io/github/actions/workflow/status/nikooozzz/passly/test.yml?label=Tests&labelColor=blue&color=midnightblue)
![AUR Status](https://img.shields.io/aur/version/passly?label=AUR)
![PyPI version](https://img.shields.io/pypi/v/passly)

---

## Features (MVP)

- Import Bitwarden CSV exports
- Detect duplicate password entries
- Identify multiple accounts on the same domain (basic subdomain handling)
- Generate a human-readable report
- Simple CLI interface with flags to choose checks

---

## Installation

### From PyPi (recommended)

```bash
pip install passly
```

### From Source

```bash
git clone https://github.com/nikooozzz/passly.git
cd passly
pip install .
```

### Arch Linux (AUR)
```bash
sudo pacman -S passly
```

---

## Usage
```bash
passly <path-to-csv> --output <path-to-output-file> --check duplicates,multi_accounts
```

### Common flags
- `--input`: Path to the CSV file to import.
- `--check`: Comma-separated list of checks to run (e.g., `duplicates,multi_accounts`).
- `--output`: Optional path to save the report (default: stdout).
- `--color` : Toggle color output (default: color).

---

## Contributing
Contributions welcome! Please see [CONTRIBUTING](CONTRIBUTING.md) for details.

---

## License
MIT License Copyright (c) 2025 nikooozzz

