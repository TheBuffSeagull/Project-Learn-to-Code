from tabnanny import check
import requests
import re
import json

#this is attempt two cause I said fuck it and started over

def clean_up(paste):
    """cleans off the bullshit from the init paste"""
    cleaning_front = paste.replace('<indent=2%>', '')
    cleaning_back = cleaning_front.replace('</indent>', '')
    final_cleaned_up_version = cleaning_back.replace('<color="orange">[YOU]</color>', '')
    print(final_cleaned_up_version)

    return final_cleaned_up_version


def save_to_file(final):
    # reading the data from the file
    with open('USERNAMES.txt') as f:
        data = f.read()
    
    print("Grabbing main Dictionary from file as str: ", type(data))
        
    # reconstructing the data as a dictionary
    main_dictionary = json.loads(data)
    
    print("Reconstructing as dictionary: ", type(main_dictionary))

    print("Merging new data to primary file...")

    save_file = main_dictionary | final

    with open("USERNAMES.txt", "w") as f_w:
        f_w.write(json.dumps(save_file))
        print(f"File edited with {save_file}.\n\n\n")

def check_dup(item_list, item):
    seen = set(item_list)

    # [...]

    if item not in seen:
        seen.add(item)
        item_list.append(item)

origin_dict = {}
used_list = []

Active = True


while Active: 
    string = input("save, add, search, or exit:  ")

    if string == "save":
        save_to_file(origin_dict)

    if string == "add":
        edit_mode = True
        while edit_mode:
            edit = clean_up(input("Add data or exit: "))
            #creating an exit
            if edit == "exit":
                edit_mode = False

            user_name = re.findall('"([^"]*)"', edit) 
            user_ID = re.findall(r'\s\[(\w+)\]', edit)

            print(f"Found {user_name} with ID {user_ID}")

            _name = "".join(user_name)
            _id = "".join(user_ID)

            print(f"Joining {_id} and {_name}\n")

            if _id not in origin_dict:
                origin_dict[_id] = list()
            if _name not in used_list:
                origin_dict[_id].append(_name)


            seen = set(used_list)
            used_list.append(_name)

            print(f"Current dictionary is: {origin_dict}\n\n")

    if string == "search":

        lookup = input("Please enter the User's ID: ")
        try:
            print(origin_dict.get(lookup))
        except:
            print("Data was not found")

    if string == "exit":
        Active = False
