# What is this
This is a capstone project I am working on, the main goal is to make a fun toy that is inspired by the tamagotchi. I plan to open source this project to allow people to tinker and learn.

# Required materials
 * Raspberry pi Zero 
 * BME 680
 * OLED 

# Future Ideas
The doogit product should come with a instruction manual, advertise this product like the 1975 pet rock. <br />
Since Raspberry Pi Zero can interact with wifi, I plan on making the doogit connect to a home hosted webserver to add friends and such. Soon we can use RFID tags to friend doogits by simply bringing the device close to eachother. The global doogit server or "official" will be hosted on my home IP but anybody should be allowed to host, I will add another file for serverside hosting setup.<br />
Better organization


# For tinkerers

## Doogits
Doogits are contained in the "Doogits" folder, the description of each is encoded in a json file. The json files are nested dictionaries that each corrospond to different behaviour and needs. The needs dictionary are the doogit's direct stats (Water, Happy, Food). The schedule dictionary will determine what events can occure at a given time of day for the doogit. The traits dictionary can describe the Doogit's status effects and unique traits

## base.json
Base is a json file that describes events and traits, it is compiled by the python code to know the properties of the doogit

## screen.py
A class that manages the OLED screen, This is a class incase we want to manage multiple screens

## sensor.py
A class that manages the sensors, This is a class incase we want to manage multiple sensors

## user_state.json
Contains the users data, will be used to store currency and the current state of the machine
