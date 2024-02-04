#!/bin/bash

image_path=$(grep -o 'file=.*' ~/.config/nitrogen/bg-saved.cfg -m 1 | cut -d'=' -f2)
cfg_path=$HOME/.config/i3/config

python main.py -p $image_path -n 9 -i $cfg_path

i3-msg restart




