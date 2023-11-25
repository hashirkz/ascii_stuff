#!/usr/bin/bash
sudo apt update
sudo apt install python3.8
pip3 install -r 'requirements.txt'

sudo cp ./app.py $HOME/.local/bin/ascii