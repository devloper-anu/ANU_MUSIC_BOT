#!/bin/bash

# Remove existing virtual environment
rm -rf .venv

# Create a fresh virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Start the bot
python bot.py
