from turtle import clear
import requests
import re
import json




idlist = {}


def clean_up(paste):
    """cleans off the bullshit from the init paste"""
    print('Clean up results:\n')
    cleaning_front = paste.replace('<indent=2%>', '')
    cleaning_back = cleaning_front.replace('</indent>', '')
    final_cleaned_up_version = cleaning_back.replace('<color="orange">[YOU]</color>', '')
    print(final_cleaned_up_version)

    return final_cleaned_up_version


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

    return page.text

def save_to_file():
    with open("USERNAMES.txt", "w") as file:
        file.write(json.dumps(origin_dict))
        print(f"File edited with {origin_dict}.\n\n\n")

def list_dup_removal(input_list):
    # using naive method
    # to remove duplicated 
    # from list 
    res = []
    for i in input_list:
        if i not in res:
            res.append(i)

    print(res)
    return res


#make dictionary
origin_dict = {}

try:
    origin_dict = read_file()
except:
    print("no inital dictionary")


carrier = clean_up(input("Copy into Storage: "))

string = carrier.split('\n')

list_dup_removal(string)



print(f"Printing string: {string}\n\n\n")

for line in string:
    user_name = re.findall('"([^"]*)"', line) 
    user_ID = re.findall(r'\s\[(\w+)\]', line)

    print(f"Found {user_name} with ID {user_ID}\n")
    #make lists to tuples to avoid error
    
    _name = "".join(user_name)
    _id = "".join(user_ID)

    print(f"Joining {_id} and {_name}")

    if _id not in origin_dict:
        origin_dict[_id] = list()
    origin_dict[_id].append(_name)


print(f"final product: {origin_dict}\n\n\n")

save_to_file()



