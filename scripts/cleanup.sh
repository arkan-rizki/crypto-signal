#!/bin/bash
find ./storage/logs -type f -name "*.log" -size +5M -exec rm -f {} \;
echo "Logs cleaned."
