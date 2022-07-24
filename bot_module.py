# importing the modules
import os
import pandas as pd
import json
import re

Current_directory = os. getcwd()

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

def write_name_storage(data):
    with open("NAME_STORAGE.txt", "r+") as storage:
        file = storage.read()


        #place holder if nothing in file
        Dictionary = {}
    
        try:
            #using json.loads to convert file to dictionary
            Dictionary = json.loads(file)
            
        #sometimes if file empty we get an exception
        except Exception as e: print(e)
        
        #return_info = []
        return_dict = dict()
        df_list = list()
        names_added = 0

        for item in data:
            _id = item[0]
            _name = item[1]
        
            #ID process
            if _id not in Dictionary.keys():
                print(f"adding id: {_id}")
                Dictionary[_id] = list()

            #Name Process
            if _name not in Dictionary.get(_id):
                print(f"adding name: {_name}")
                names_added += 1
                Dictionary[_id].append(_name)
        
            #return_info.append(f"{_id}:\n{', '.join(Dictionary[_id])}\n")

            df_list.append(_id)
        
        #move back to first line of file
        storage.seek(0)
        #Write dictionary to Name_STORAGE.txt 
        # (dumps makes dictionary to str cause you can't write DICT to file)
        storage.write(json.dumps(Dictionary))
        #truncate makes sure the file is now the size of "Dictionary" (sometimes old stuff was left behind)
        storage.truncate()
        
        
        
        #number of names to add the <br/> after
        n=3
        for id_object in df_list:
            #add names from find names fuction to list
            #converting set to remove duplicate values
            names = find_names(id_object)
            if len(names) > 1:
                names = [n+"," for n in names]
            else:
                pass

            names = list(' '.join(i + "<br/>" * (n % 3 == 2) for n, i in enumerate(names)))
            #now were fucking coding! we are joining a bunch of shit here to basically add a <br/> every 3 names
            return_dict[id_object] = ''.join(names)

        print(f"{names_added} new names added")
        return return_dict, names_added

    

def get_paste(data):  
    """Takes paste data from discord and adds it to dictionary."""
    #Cleaning this as the RE module finds it.
    data = data.replace('<color="orange">[YOU]</color>', '')
    if data.startswith('<indent=2%>'):

        #SPECIFYING THESE BEFORE CLEANING TO AVOID BAD BRACKETS BEING ADDED LIKE HOST DATA NUMBERS Ex: '[01] -'
        user_name = re.findall('"([^"]*)"', data) 
        user_ID = re.findall(r'\s\[(\w+)\]', data)


        data = merge(user_ID, user_name)

        return_info = write_name_storage(data)

        return return_info

    else:
        return
    



def find_names(id):
    """Makes a DataFrame using Pandas and then searches for a column with the ID name given.
    Then it returns to the bot the names in a list to be displayed in Discord"""
    with open(rf"{Current_directory}\NAME_STORAGE.txt") as file:
        data = file.read()
        name_storage = json.loads(data)
        
    df = pd.DataFrame.from_dict(name_storage, orient='index')
    df = df.transpose()


    try:
        #using id to create list of names found
        names_found = df[id].to_list()
    except KeyError:
        names_found = ''
    
    # using list comprehension
    # to remove None values in list
    names_found = [i for i in names_found if i]

    return names_found

       

#find_names('00029786edf14144b1375e75bdd406e1')
#info = get_paste('<indent=2%>"Chocato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[YAK]Chocato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[Boom]Chocato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[RA]Chocato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[AK4]Chocato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[SPIN]Chocato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[RQM]Chocato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Faye"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[RRC]Hanako"   [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[ES]Chocato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[ES]Korra"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Misato"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Swordsop"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Trainee"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"NOTdorito"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Bruh"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Ihatemyself"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Katara"   [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Asuka"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Kumiko"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"NOTSaya"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Cheese"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"NotSteq"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"MrSandwich"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"Pringl[es]"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"[ES]Parona"  [0002fb4f0b244828a7513617f9d61f38]</indent><indent=2%>"THEtrainee"   [0002fb4f0b244828a7513617f9d61f38]</indent>')

#for line in info:
#    print(line)


