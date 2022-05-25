from rich import print
from pathlib import Path
import pprint
import re
import json
import os


def get_paste_doc():  
    #Try on open to read paste file and then clear the contents
    with open('PASTE_DOC.txt', 'r') as f:
        data = f.read()
        print("Grabbing paste data from file as str: ", type(data))

        #SPECIFYING THESE BEFORE CLEANING TO AVOID BAD BRACKETS BEING ADDED LIKE HOST DATA NUMBERS Ex: '[01] -'
        user_name = re.findall('"([^"]*)"', data) 
        user_ID = re.findall(r'\s\[(\w+)\]', data)
        
        cleaning_front = data.replace('<indent=2%>', '')
        cleaning_back = cleaning_front.replace('</indent>', '\n')
        #replacing personal color
        data = cleaning_back.replace('<color="orange">[YOU]</color>', '')

        if len(user_ID) > 1:
            print(f"Found {user_name} with ID {user_ID}\n")
                            
        data = merge(user_ID, user_name)


        for _id, _name in data:
            if _id not in Dictionary:
                Dictionary[_id] = list()       
            
            #seen list is making it so that you can't have two people with the same name
            if _name not in seen_list:
                Dictionary[_id].append(_name)
                #add name to seen list after adding
                seen_list.append(_name)

            if len(user_ID) > 1:
                pprint.pprint(Dictionary)


        return Dictionary

def merge(list1, list2):
      
    merged_list = []
    for i in range(max((len(list1), len(list2)))):
  
        while True:
            try:
                tup = (list1[i], list2[i])
            except IndexError:
                if len(list1) > len(list2):
                    list2.append('')
                    tup = (list1[i], list2[i])
                elif len(list1) < len(list2):
                    list1.append('')
                    tup = (list1[i], list2[i])
                continue
  
            merged_list.append(tup)
            break
    return merged_list

#making sure the file exists with touch before opening it
Path('NAME_STORAGE.txt').touch(exist_ok=True)




with open("NAME_STORAGE.txt", "r+") as file:
    data = file.read()

    print("Grabbing main dictionary from file. Expecting str: ", type(data))

    #place holder if nothing in file
    Dictionary = {}

    #seen list is to prevent duplicates
    seen_list = []
    #look for new entries from paste_DOC to add to dictionary before checking if empty
    paste_doc = get_paste_doc()
    Dictionary = Dictionary | paste_doc

    #using this to skip json.loads if no data
    file_empty = os.stat("NAME_STORAGE.txt").st_size == 0

    if file_empty == False:
        #using json.loads to convert file to dictionary
        Dictionary = json.loads(data)
        print("Expecting Dictionary: ", type(Dictionary))
    else:
        print("Error: There is no file data.")
    
    #Print dictionary to console
    pprint.pprint(Dictionary)
    #get current number of entries
    print(f"File currently has {len(Dictionary)} values.\n")


        



