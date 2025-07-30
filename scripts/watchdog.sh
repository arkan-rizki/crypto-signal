#!/bin/bash
while true; do
  pgrep -f main.py > /dev/null
  if [ $? -ne 0 ]; then
    echo "[Watchdog] Restarting..."
    python3 main.py
  fi
  sleep 20
done
