# BellAvr-RVR-Code

# Downloading
git clone --recurse-submodules https://github.com/The-Coding-Cod/BellAvr-RVR-Code
Ensure you have the submodules from SpheroSDK, the PCA9685 module is already packaged

# Setup
It is recommended to hook the PCA9685 up to another power supply, but it is not required. The two continous servos go on channels 0 and 1 while the positional one is on channel 2. Follow the SpheroSDK guide for hooking up the Pi to the RVR

# Calibrating
To calibrate, run the calibration.py and then note which inputs do what. Then Fill them in on the Json file. If one of the servos runs in reverse go to the spefic spot where the function is called and change the 3rd argument to True. Note that the servo reverse for slot 0 and 1 use triggers or someother axis, while the other servo functions use joybuttons

# Running
Run it using a monitor or setup Xfvb on the pi for running it from SSH

# Adding SSH
__In order to SSH from anywhere, you need to get the Pi to host its own network. Here's how through commands:__

sudo systemctl stop wpa_supplicant  
sudo systemctl disable wpa_supplicant

sudo nano /etc/dhcpcd.conf

__Add to bottom of file:__

interface wlan0  
static ip_address=192.168.4.1/24  
nohook wpa_supplicant

__Save that and Exit__

sudo nano /etc/hostapd/hostapd.conf

__You will see (or must add):__

interface=wlan0  
driver=l80211  
ssid= !ADD WIFI NAME HERE!  
hw_mode=g  
channel=7  
auth_algs=1  
wpa=2  
wpa_passphrase=!ADD PASSWORD HERE!  
wpa_key_mgmt=WPA-PSK  
rsn_pairwise=CCMP

__Save and Exit__

sudo systemctl enable hostapd  
sudo systemctl enable dnsmasq

sudo systemctl start hostapd  
sudo systemctl start dnsmasq

sudo systemctl restart dhcpcd

sudo reboot

__Now to get updates for this repo, you need to connect again. Here's how through the command prompt:__

sudo systemctl stop hostapd  
sudo systemctl stop dnsmasq

sudo systemctl disable hostapd  
sudo systemctl disable dnsmasq

sudo nano /etc/dhcpcd.conf

__Comment this out with #:__

interface wlan0  
static ip_address=192.168.4.1/24  
nohook wpa_supplicant

__Save and Exit__

sudo systemctl enable wpa_supplicant  
sudo systemctl start wpa_supplicant

sudo systemctl restart dhcpcd

sudo reboot

__You should now be able to connect to wifi__
