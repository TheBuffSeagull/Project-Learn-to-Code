from rich import print
import pprint
import re
import json
import os

#this is attempt two cause I said fuck it and started over


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def clean_up(paste):
    """cleans off the bullshit from the init paste"""
    cleaning_front = paste.replace('<indent=2%>', '')
    cleaning_back = cleaning_front.replace('</indent>', '')
    final_cleaned_up_version = cleaning_back.replace('<color="orange">[YOU]</color>', '')

    return final_cleaned_up_version


def save_to_file(final):
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

        print("Merging new data to primary save file...")
    except:
        print("No data in main dictionary...") 

    # reconstructing the data as a dictionary


    save_file = main_dictionary | final

    with open("USERNAMES.txt", "w") as f_w:
        f_w.write(json.dumps(save_file))


    print(f"File currently has {len(save_file)} values.\n\n\n")


origin_dict = {}
used_list = []

Active = True


while Active: 
    string = input("add, search, or exit: ")

    if string == "add":
        edit_mode = True
        while edit_mode:
            edit = clean_up(input("Add data or save: "))
            #creating an exit
            if edit == "save":
                save_to_file(origin_dict)
                edit_mode = False
                break
            
            user_name = re.findall('"([^"]*)"', edit) 
            user_ID = re.findall(r'\s\[(\w+)\]', edit)

            print(f"Found {user_name} with ID {user_ID}\n")

            _name = "".join(user_name)
            _id = "".join(user_ID)


            if _id not in origin_dict:
                origin_dict[_id] = list()
            if _name not in used_list:
                origin_dict[_id].append(_name)


            seen = set(used_list)
            used_list.append(_name)


    if string == "search":
        lookup_mode = True
        while lookup_mode:
            lookup = input("Please enter the User's ID, type 'all', or 'back': ")
            if lookup == "back":
                lookup_mode = False
                cls()
            
            elif lookup == "all":
                try:
                    with open('USERNAMES.txt') as f:
                        dictionary_data = f.read()
                        pprint.pprint(dictionary_data)
                except:
                    print("No data")
            else:
                try:
                    with open('USERNAMES.txt') as f:
                        dictionary_data = f.read()
                        pprint.pprint(dictionary_data.get(lookup))
                except:
                    print("No data")

    if string == "exit":
        Active = False
