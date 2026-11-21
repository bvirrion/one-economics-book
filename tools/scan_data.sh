#!/usr/bin/env bash
# Scan data/raw/ with Windows Defender from WSL (user rule, 2026-11-20: downloaded data
# may be scanned; fetch_data.py already rejects macros, executables and unsafe archives).
# Prints Defender's verdict; exit 0 when no threat is found.
set -u
cd "$(dirname "$0")/.."
MP="/mnt/c/Program Files/Windows Defender/MpCmdRun.exe"
[ -x "$MP" ] || { echo "Windows Defender not found (not WSL?)"; exit 2; }
distro=${WSL_DISTRO_NAME:-Ubuntu}
target="\\\\wsl.localhost\\$distro$(pwd | sed 's|/|\\|g')\\data\\raw"
"$MP" -Scan -ScanType 3 -File "$target" -DisableRemediation | tr -d '\r'
