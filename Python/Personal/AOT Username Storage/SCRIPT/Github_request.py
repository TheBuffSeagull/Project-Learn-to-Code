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

def ids_for_usernames(ids):
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

def save_to_file():
    with open("USERNAMES.txt", "w") as file:
        file.write('\n')
        file.write(json.dumps(origin_dict))
        print(f"File edited with {origin_dict}.")



url = 'https://raw.githubusercontent.com/TheBuffSeagull/Project-Learn-to-Code/master/Python/Personal/AOT%20Username%20Storage/AOT_NAMES_DUMP.txt'
page = requests.get(url)

string = clean_up(page.text)

user_IDS, user_names = ids_for_usernames(string)

print("\nMAKING DICTIONARY -----------------")
# using naive method
# to convert lists to dictionary
idlist = {user_IDS[i]: user_names[i] for i in range(len(user_IDS))}


print(idlist)
print(origin_dict)

# reading the data from the file
with open('USERNAMES.txt', "r") as f:
    data = f.read()

  
    print("Data type before reconstruction : ", type(data))
        
    # reconstructing the data as a dictionary
    js = json.loads(data)
    
    print("Data type after reconstruction : ", type(js))
    print(js)
    origin_dict = js


origin_dict.update(idlist)

save_to_file()

#Names = True
#while Names is True:
#    print(f"Program running....")
