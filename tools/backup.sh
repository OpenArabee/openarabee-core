#!/usr/bin/env bash
# Write a complete, verified git bundle of this repository (charter §8, D-011).
# Usage: tools/backup.sh [output directory]   (default: build/)
# The bundle is then uploaded to the Google Drive folder "OpenArabee-Backups".
# Restore with: git clone <file>.bundle <directory>
set -euo pipefail
repo_root="$(git rev-parse --show-toplevel)"
name="$(basename "$repo_root")"
out_dir="${1:-$repo_root/build}"
mkdir -p "$out_dir"
bundle="$out_dir/$name-$(date -u +%Y%m%d-%H%M).bundle"
git -C "$repo_root" bundle create "$bundle" --all
git -C "$repo_root" bundle verify "$bundle"
echo "$bundle"
