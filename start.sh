#!/bin/bash

rm -rf .venv
python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install --no-cache-dir --force-reinstall -r requirements.txt

python bot.py
