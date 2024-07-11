#!/bin/bash

# URL script Python
SCRIPT_URL="https://raw.githubusercontent.com/masjeho2/pingfud/main/shopeefud.py"

# Nama file untuk menyimpan script Python
SCRIPT_FILE="shopeefud.py"

# Mengunduh script Python
curl -O $SCRIPT_URL

# Menjalankan script Python
python $SCRIPT_FILE
