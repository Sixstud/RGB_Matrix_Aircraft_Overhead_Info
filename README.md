once install sh has been made - make it executable
chmod +x install.sh


Flight Radar Matrix Display

A Raspberry Pi Zero W project displaying aircraft within 15 miles on a 64x32 RGB LED matrix.

Hardware
- Raspberry Pi Zero W
- Adafruit RGB Matrix Bonnet
- 64x32 HUB75 RGB LED panel

Features
- Aircraft detection using OpenSky API
- Radar sweep animation
- Flight number display
- Distance and altitude
- Airline colour coding
- Weather fallback when no aircraft nearby
- Automatic brightness dimming
- Systemd autostart

Installation

git clone https://github.com/YOURNAME/flight-radar-matrix.git
cd flight-radar-matrix

chmod +x install.sh
./install.sh

Reboot.

Then install the service:

chmod +x service_install.sh
sudo ./service_install.sh



To install 

git clone https://github.com/yourusername/flight-radar-matrix.git
cd flight-radar-matrix

chmod +x install.sh
./install.sh

if the RGB Matrix oes not work due to missing binding - eg module RGB Matrix cannot be found then rund this

cd ~/rpi-rgb-led-matrix/bindings/python
sudo pip3 install . --break-system-packages

