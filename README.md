# redshift-Control
A xfce environment utility that controls redshift to adjust the bluelight emitted by the screen .
Using this utility you can easily control the redshift to adjust screen temperature. 

##  IMP - Prerequisite ##
* Make sure that python is installed in your machine.
```bash
  sudo apt update
  sudo apt upgrade
  sudo apt install python3
```
## Installation
```bash
  git clone git@github.com:shivamdangi7/redshift-Control.git
  cd redshift-Control
  cp -r redshift-control/ ~/.config/
  sudo cp redshift-control.py /usr/local/bin/
```
Next steps
cd into `cd /usr/share/applications/` directory
make a file name `redshift-control.desktop` `touch redshift-control.desktop`
edit this file with your text editor with sudo previlages.
and put the below text into it .
```bash
[Desktop Entry]
Version=9.0
Type=Application
Name=Redshift Control
Comment=Control Redshift color temperature
Exec=python3 /usr/local/bin/redshift-control.py
Icon=/home/<yourUserName>/.config/redshift-control/redshift-control.svg
Terminal=false
Categories=Utility;
StartupNotify=true
```
Make sure to edit <yourUserName> with your own user name like [sdangi@Who-Delusion ~] sdangi here is my username.
Now you can control your screen tempereture with just a scroll of your mouse.
Enjoy.
  
#Add redshift-Control at startup.
 * Go to startup in whisker menu.
 * Go to Application Autostart.
 * Click on + icon.
 * Add the following :
  ```
    Name : Redshift Control
    Description : Control Screen Temperature 
    Command : python3 /usr/local/bin/redshift-control.py
  ```
  * Press OK
 
 
