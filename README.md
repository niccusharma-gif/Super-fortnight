# Duplicate File Finder

Find duplicate files by content hash and export a review report.

## Features

- Larger workspace with action buttons, result panel, and activity log.
- Shared theme selector: Graphite, Crimson Night, Ocean, Forest, Violet, Light, Solarized, or custom colors.
- Theme preferences are shared across all 32 apps on the same user account.
- Uses safe defaults: preview/confirmation for file or system changes where applicable.

## Run on Ubuntu / Debian

Install the Qt bindings from your distribution package manager (recommended if pip downloads are unreliable):

```bash
sudo apt update
sudo apt install -y python3 python3-pyside6.qtwidgets python3-pyside6.qtgui python3-pyside6.qtcore
cd 08_duplicate_file_finder
/usr/bin/python3 main.py
```

Some projects optionally use system commands or tools. Missing tools are reported instead of silently pretending to work.

## Run on Windows

Install Python 3.10+ and then run in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

## Notes

This is a functional hobby-project suite, not a production-certified application. OS-specific features are detected and may be unavailable on some systems. Review confirmations before moving files, installing packages, changing startup entries, or launching commands. Keep backups of important data.
