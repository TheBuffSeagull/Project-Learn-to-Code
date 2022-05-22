import requests
import re
import json
import os


origin_dict = {}
idlist = {}

dir_path = os.path.dirname(os.path.realpath(__file__))

print(f"Current working directory is: {dir_path}")

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
    for _name in user_names:
        for _ID in user_IDS:
            return _name, _ID

def read_file():
    # reading the data from the file
    with open('USERNAMES.txt', "r") as f:
        data = f.read()

  
        print("Data type before reconstruction : ", type(data))
        
        # reconstructing the data as a dictionary
        js = json.loads(data)
    
        print("Data type after reconstruction : ", type(js))
        print(js)

def save_to_file():
    with open("USERNAMES.txt", "w") as file:
        file.write('\n')
        file.write(json.dumps(origin_dict))
        print(f"File edited with {origin_dict}.")





# reading the data from the file
with open('USERNAMES.txt', "r") as f:
    data = f.read()

  
    print("Data type before reconstruction : ", type(data))
        
    # reconstructing the data as a dictionary
    js = json.loads(data)
    
    print("Data type after reconstruction : ", type(js))
    print(js)
    origin_dict = js


url = 'https://raw.githubusercontent.com/TheBuffSeagull/Project-Learn-to-Code/master/Python/Personal/AOT%20Username%20Storage/AOT_NAMES_DUMP.txt'
page = requests.get(url)


string = clean_up(page.text)


_ID, _name = Usernames(string)

print(_ID)
print(_name)

for key, val in origin_dict.items():
    if _ID not in key:
        




print(f"final product: {origin_dict}")

save_to_file()



