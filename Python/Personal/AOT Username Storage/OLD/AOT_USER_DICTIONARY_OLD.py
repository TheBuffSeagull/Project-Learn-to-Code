from rich import print
import pprint
import re
import json
import os
import sys
import psutil
import logging


#this is attempt two cause I said fuck it and started over


def clean_up(paste):
    """cleans off the bullshit from the init paste"""
    cleaning_front = paste.replace('<indent=2%>', '')
    cleaning_back = cleaning_front.replace('</indent>', '\n')
    final_cleaned_up_version = cleaning_back.replace('<color="orange">[YOU]</color>', '')

    return final_cleaned_up_version

def save_to_file(final):
    # reading the data from the file
    with open('USERNAMES.txt') as f:
        data = f.read()
    
    print("Grabbing main dictionary from save file as str: ", type(data))
    #place holder if nothing in file
    main_dictionary = {}
    # reconstructing the data as a dictionary
    try:
        main_dictionary = json.loads(data) 
       # reconstructing the data as a dictionary

        print("Reconstructing as dictionary: ", type(main_dictionary))

    except:
        print("No data in main dictionary...") 

    # reconstructing the data as a dictionary

    print("Saving new entries from paste file...")
    save_file = final
    print(f"File currently has {len(save_file)} values.\n")

    with open("USERNAMES.txt", "w") as f_w:
        f_w.write(json.dumps(save_file))

def read_from_file():
    # reading the data from the file
    with open('USERNAMES.txt') as f:
        data = f.read()
    
    print("Grabbing main dictionary from file as str: ", type(data))
    #place holder if nothing in file
    main_dictionary = {}
    # reconstructing the data as a dictionary
    try:
        main_dictionary = json.loads(data) 
       # reconstructing the data as a dictionary

        print("Reconstructing as dictionary: ", type(main_dictionary))
    
        pprint.pprint(main_dictionary)
        print(f"File currently has {len(main_dictionary)} values.\n")
        
        return main_dictionary

    except:
        print("Something went wrong...")

def read_paste_file():
    with open('PASTE_DOC.txt', 'r') as f:
        data = f.read()
        print("Grabbing paste data from file as str: ", type(data))
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

def update_USERNAMES():  
    #Try on open to read paste file and then clear the contents
    try:
        edit = read_paste_file()
        _edit = clean_up(edit)

        user_name = re.findall('"([^"]*)"', _edit) 
        user_ID = re.findall(r'\s\[(\w+)\]', _edit)
        if len(user_ID) > 1:
            print(f"Found {user_name} with ID {user_ID}\n")
                        
        import_data = merge(user_ID, user_name)

        for _id, _name in import_data:
            if _id not in origin_dict:
                origin_dict[_id] = list()       
            if _name not in added_names:
                origin_dict[_id].append(_name)
                added_names.append(_name)

        if len(user_ID) > 1:
            pprint.pprint(origin_dict)


        return origin_dict
        
    except Exception as e: print(e)


    python = sys.executable
    os.execl(python, python, *sys.argv)

origin_dict = {}
dictionary_data = {}
used_list =[]

Active = True

#On Startup
origin_dict = update_USERNAMES()

dictionary_data = read_from_file()

print(f"Content to update: {origin_dict | dictionary_data}")
check_data = origin_dict | dictionary_data
print("Checking data type: ", type(check_data))
save_to_file(check_data)


#ACTIVE PROGRAM
while Active:

        origin_dict = update_USERNAMES()

        dictionary_data = read_from_file()


        string = input("Type an AOT User ID, 'all', 'remove', or 'exit': ")

        if string == "remove":
            try:
                print("\nWARNING: REMOVE FUNCTION CLEARS PASTE_DOC. DATA STILL STORED IN USERNAMES.TXT\n")
                remove_ID = input("Type an ID to remove: ")
                print(f"Deleting {remove_ID} with names {dictionary_data[remove_ID]}")
                del dictionary_data[remove_ID]
                del origin_dict[remove_ID]
                #updates after removal 
                print(f"Content to update: {origin_dict | dictionary_data}")

            except Exception as e: print(e)
        
        
        elif string == "all":
            try:
                pprint.pprint(dictionary_data)
            except Exception as e: print(e)
    

        elif string in dictionary_data:
            print(dictionary_data[string])
        
        elif string == "exit":
            with open('PASTE_DOC.txt', 'w') as f_P:
                    f_P.write('')
            Active = False

