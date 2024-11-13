# !/usr/bin/bash
. .venv/bin/activate
python3 ./src/makepdf.py $(cd $(dirname $0); pwd)
deactivate