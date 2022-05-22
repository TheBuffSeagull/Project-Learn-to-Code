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
    cleaning_back = cleaning_front.replace('</indent>', '\n')
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

    print("Saving new file...")
    save_file = main_dictionary | final

    with open("USERNAMES.txt", "w") as f_w:
        f_w.write(json.dumps(save_file))


    print(f"File currently has {len(save_file)} values.\n\n\n")

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


origin_dict = {}
used_list = []

Active = True


try:
    edit = read_paste_file()
    _edit = clean_up(edit)

    user_name = re.findall('"([^"]*)"', _edit) 
    user_ID = re.findall(r'\s\[(\w+)\]', _edit)

    print(f"Found {user_name} with ID {user_ID}\n")
                    
    import_data = merge(user_ID, user_name)

    for _id, _name in import_data:
        if _id not in origin_dict:
            origin_dict[_id] = list()       
        if _name not in used_list:
            origin_dict[_id].append(_name)
            used_list.append(_name)

    pprint.pprint(origin_dict)
except Exception as e: print(e)


while Active: 
    string = input("Type an ID, 'all', or 'exit': ")

    if string == "add":
        edit_mode = True
        while edit_mode:
            edit = input("'import' or 'save': ")
            if edit == "import":
                try:
                    edit = read_paste_file()
                    _edit = clean_up(edit)

                    user_name = re.findall('"([^"]*)"', _edit) 
                    user_ID = re.findall(r'\s\[(\w+)\]', _edit)

                    print(f"Found {user_name} with ID {user_ID}\n")
                    
                    import_data = merge(user_ID, user_name)

                    for _id, _name in import_data:
                        if _id not in origin_dict:
                            origin_dict[_id] = list()       
                        if _name not in used_list:
                            origin_dict[_id].append(_name)
                            used_list.append(_name)

                    pprint.pprint(origin_dict)
                except Exception as e: print(e)
            
            #creating an exit
            if edit == "save":
                cls()
                save_to_file(origin_dict)
                edit_mode = False
                break


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
