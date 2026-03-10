#!/bin/bash

echo "Updating system"
sudo apt update

echo "Installing dependencies"
sudo apt install -y python3-pil python3-requests git

echo "Installing RGB matrix driver"

curl -sSL https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/rgb-matrix.sh > /tmp/rgb-matrix.sh
sudo bash /tmp/rgb-matrix.sh

echo "Disabling audio for stable matrix timing"

if ! grep -q "dtparam=audio=off" /boot/config.txt; then
echo "dtparam=audio=off" | sudo tee -a /boot/config.txt
fi

echo "Install complete. Please reboot."

echo "sudo reboot"
