from rich import print
from pathlib import Path
import pprint
import re
import json


def get_paste(data):  
    """TAKES AOT USER PASTE AND MAKES IT USABLE AS DICTIONARY."""
    #Try on open to read paste from user and then clear the contents
    print("Grabbing paste data input as str: ", type(data))

    #Cleaning this as the RE module finds it.
    data = data.replace('<color="orange">[YOU]</color>', '')
    
    #SPECIFYING THESE BEFORE CLEANING TO AVOID BAD BRACKETS BEING ADDED LIKE HOST DATA NUMBERS Ex: '[01] -'
    user_name = re.findall('"([^"]*)"', data) 
    user_ID = re.findall(r'\s\[(\w+)\]', data)
    
    data = data.replace('<indent=2%>', '')
    data = data.replace('</indent>', '\n')


    data = merge(user_ID, user_name)
    #maybe turn data into set to avoid duplicatesa
    print(f'Data ftom function: {data}')



    #This returns a list with ID first and name second
    return data

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
    paste_doc = {}
 
    try:
        #using json.loads to convert file to dictionary
        Dictionary = json.loads(data)
        print("Converting back to Dictionary. Expecting Dictionary: ", type(Dictionary))
        
    #sometimes if file empty we get an exception
    except Exception as e: print(e)


    Active = True
    while Active:
        
        user_input = input("Type an AOT User ID, 'add', 'all', 'remove', or 'exit': ")

   
        if user_input == 'add':
            while True:
                paste_input = input("Please paste new data into window or type 'save': ")
                
                #check for user exit before process.
                if paste_input == 'save':
                    #save current stage in case someone closes the program without typing exit
                    try:
                        #merging current updated dictionary and paste entries dictionary
                        Dictionary = Dictionary | paste_doc
                    except Exception as e: print(e)


                    #move back to first line of file
                    file.seek(0)
                    #Write dictionary to Name_STORAGE.txt 
                    # (dumps makes dictionary to str cause you can't write DICT to file)
                    file.write(json.dumps(Dictionary))
                    #truncate makes sure the file is now the size of "Dictionary" (sometimes old stuff was left behind)
                    file.truncate()
                    #get current number of entries
                    print(f"File has updated to have {len(Dictionary)} values.\n")
                    
                    break
                
                #look for new entries from user paste
                paste_doc = get_paste(paste_input)
                print(f'Data ftom paste_doc function: {paste_doc}')

                paste_doc = set(paste_doc)
                print("Expecting Set: ", type(paste_doc))
                print(f'Data ftom set: {paste_doc}')

                for _id, _name in paste_doc:
                    if _id not in Dictionary.keys():
                        Dictionary[_id] = list()
                        print(f"Adding Dictionary ID: {_id}")       
                    if _name not in Dictionary.get(_id):
                        Dictionary[_id].append(_name)
                        print(f"Adding Name: {_name}")
                


        
        if user_input == "remove":
            while True:
                try:
                    remove_input = input("Type an ID to remove or 'back': ")
                    
                    #check for user exit before paste data.
                    if remove_input == 'back':
                        break
                    
                    #otherwise we deleting
                    else:
                        try:
                            print(f"Deleting {remove_input} with names {Dictionary[remove_input]}")
                            del Dictionary[remove_input]
                        #gotta catch em all!
                        except Exception as e: print(e)

                except Exception as e: print(e)
        
        if user_input == 'all':
            pprint.pprint(Dictionary)
            print(f"File currently has {len(Dictionary)} values.\n")

        #get user ID if someone looks it up
        elif user_input in Dictionary:
            if len(Dictionary[user_input]) > 1:
                print(f"Found names: {Dictionary[user_input]}")

            elif len(Dictionary[user_input]) == 1:
                print(f"Found name: {Dictionary[user_input]}")
            
        elif user_input not in Dictionary:
            if "000" in user_input:
                print("No ID found.")

        if user_input == 'exit':
            Active = False
    
    
    
    #Start closing the program
    try:
        #merging current updated dictionary and paste entries dictionary
        Dictionary = Dictionary | paste_doc
    except Exception as e: print(e)


    #move back to first line of file
    file.seek(0)
    #Write dictionary to Name_STORAGE.txt 
    # (dumps makes dictionary to str cause you can't write DICT to file)
    file.write(json.dumps(Dictionary))
    #truncate makes sure the file is now the size of "Dictionary" (sometimes old stuff was left behind)
    file.truncate()
    #get current number of entries
    print(f"File has updated to have {len(Dictionary)} values.\n")


        



