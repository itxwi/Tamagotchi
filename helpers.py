import json

# HELPER FUNCTIONS

def get_userstate():
    with open("userstate.json") as file:
        global userstate
        userstate = json.load(file)
        return userstate
    
def get_doogit():
    current_doogit = get_userstate()['current_doogit']
    with open(f"doogits/{current_doogit}") as file:
        global doogit
        doogit = json.load(file)
        return doogit
    
def get_base():
    with open("base.json") as file:
        global base
        userstate = json.load(file)
        return userstate


# Initalize variables
get_userstate()
get_base()
get_doogit()

def set_doogit(doogit):
    with open("userstate.json") as file:
        json.dump(userstate,"userstate.json")
        