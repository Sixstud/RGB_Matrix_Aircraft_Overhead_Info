#!/bin/bash

sudo tee /etc/systemd/system/flightradar.service > /dev/null <<EOF
[Unit]
Description=Flight Radar Display
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/flight-radar-matrix/main.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable flightradar
sudo systemctl start flightradar

echo "Service installed and started"
