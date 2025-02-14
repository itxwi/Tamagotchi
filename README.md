## Future Ideas
The doogit product should come with a instruction manual, advertise this product like the 1975 pet rock.
Since Raspberry Pi Zero can interact with wifi, I plan on making the doogit connect to a home hosted webserver to add friends and such. Soon we can use RFID tags to friend doogits by simply bringing the device close to eachother. Maybe a way of managing transactions or shop purchases to ensure no cheating


## For tinkerers

# Doogits
Doogits are contained in the "Doogits" folder, the description of each is encoded in a json file. The json files are nested dictionaries that each corrospond to different behaviour and needs. The needs dictionary are the doogit's direct stats (Water, Happy, Food). The schedule dictionary will determine what events can occure at a given time of day for the doogit. The traits dictionary can describe the Doogit's status effects and unique traits

# Nature map
Nature map is a json folder that describes events and traits, it is compiled by the python code to know the properties of the doogit

# Screen.py
A class that manages the OLED screen, This is a class incase we want to manage multiple screens

# Sensor.py
A class that manages the sensors, This is a class incase we want to manage multiple sensors