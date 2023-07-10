#!/bin/bash

 
read -p "Enter file path: " file_address
read -p "Enter hash:: " hash

python hashchecker.py "$file_address" "$hash"


