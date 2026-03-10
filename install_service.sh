#!/bin/bash

sudo tee /etc/systemd/system/flightradar.service > /dev/null <<EOF
[Unit]
Description=Flight Radar Matrix
After=network.target

[Service]
WorkingDirectory=/home/pi/flight-radar-matrix
ExecStart=/usr/bin/python3 /home/pi/flight-radar-matrix/main.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable flightradar
sudo systemctl start flightradar
