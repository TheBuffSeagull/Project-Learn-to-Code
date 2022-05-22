import requests
import re
import json




idlist = {}


def clean_up(paste):
    """cleans off the bullshit from the init paste"""
    cleaning_front = paste.replace('<indent=2%>', '')
    cleaning_back = cleaning_front.replace('</indent>', '')
    final_cleaned_up_version = cleaning_back.replace('<color="orange">[YOU]</color>', '')
    print(final_cleaned_up_version)

    print('MADE IT THROUGH CLEAN UP\n')
    return final_cleaned_up_version

def Usernames(ids):
    """Pulls all of the information out of the brackets"""
    print('Made it to dictionary')
    
    # no idea why this works just dont fucking touch it... SERIOUSLY. 
    user_names = re.findall('"([^"]*)"', ids) 
    user_IDS = re.findall(r'\s\[(\w+)\]', ids)
    return user_IDS, user_names

def read_file():
    # reading the data from the file
    with open('USERNAMES.txt', "r") as f:
        data = f.read()

  
        print("Data type before reconstruction : ", type(data))
        
        # reconstructing the data as a dictionary
        js = json.loads(data)
    
        print("Data type after reconstruction : ", type(js))
        print(js)
        return js

def read_github():
    url = 'https://raw.githubusercontent.com/TheBuffSeagull/Project-Learn-to-Code/master/Python/Personal/AOT%20Username%20Storage/AOT_NAMES_DUMP.txt'
    page = requests.get(url)

    return clean_up(page.text)

def save_to_file():
    with open("USERNAMES.txt", "w") as file:
        file.write(json.dumps(origin_dict))
        print(f"File edited with {origin_dict}.")

def set_key(dictionary, key, value):
    """Creates dictionary without overwriting key terms"""
    if key and value not in dictionary: 
        if key not in dictionary:
            dictionary[key] = value
        if type(dictionary[key]) == list:
            dictionary[key].append(value)
        else:
            dictionary[key] = [dictionary[key], value]

def remove_dups(dictionary):
    """Making this bitch a tuple to remove the duplicates before saving"""
    list = [(k, v) for k, v in dictionary.items()]
    print("Making the dictionary into a tuple to remove duplicates...")


#make dictionary
origin_dict = dict()
#try to pull if one already exists
try:
    origin_dict = read_file()
except:
    print("no inital dictionary")


string = read_github()

user_IDS, user_names = Usernames(string)

for _ID, _name in zip(user_IDS, user_names):
    set_key(origin_dict, _ID, _name)


print(f"final product: {origin_dict}")

set(origin_dict)


save_to_file()



