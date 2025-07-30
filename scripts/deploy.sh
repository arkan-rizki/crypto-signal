#!/bin/bash
echo "[DEPLOY] Installing dependencies..."
pip install -r requirements.txt
echo "[DEPLOY] Starting system..."
python3 main.py
