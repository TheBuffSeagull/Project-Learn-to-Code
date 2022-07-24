import os
import json

def save_to(_Storage):
    with open("Usage_data.json", "w")as file:
        json.dump(_Storage, file, indent = 3)


def usage_dictionary(Discord_name, command_used): 
    """Uses Dictionary to keep track of Discord username usage data in a JSON"""
    with open("Usage_data.json", "r")as file:
        #placeholder dictionary with new discord name
        _placeholder = {
            Discord_name: {
            "lobby": 0,
            "id": 0
            }
        
        }
        #Load file
        try:
            Usage_Dictionary = json.load(file)
        except Exception:
            Usage_Dictionary = {}

        #Merge with new dicord name
        if Discord_name not in Usage_Dictionary:
            _Storage = Usage_Dictionary | _placeholder
        else:
            _Storage = Usage_Dictionary

        _Storage[Discord_name][command_used] = _Storage[Discord_name].get(command_used, 0) +1

        save_to(_Storage)

        return _Storage



#data = usage_dictionary("TheBuffBegule", "id")

#data = usage_dictionary("TheBuffBegule", "lobby")




