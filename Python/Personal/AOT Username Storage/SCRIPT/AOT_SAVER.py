from distutils.command.clean import clean
import PySimpleGUI as sg
import re
import json


idlist = {
    "ID":"USERNAME",
    }


def save_to_file():
    with open("USERNAMES.txt", "a") as file:
        file.write('\n')
        file.write(json.dumps(idlist))
        print(f"File edited with {idlist}.")


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
    
    # no idea why this works just dont fucking touch it
    user_names = re.findall(r'\>(\w+)\<', ids)

    for applicable_ID in user_names:
        idlist["ID"].append(applicable_ID)

    print(idlist)
    




layout = [
    [sg.Text('AOT Username Bank')],
    [sg.Input(key = '-INPUT-')],
    [sg.Button('Submit')]
]

window = sg.Window('Converter', layout)



while True:
    event, values = window.read()

    

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Submit':
        
        print("Button Pressed.")
        user_input = list(values.values())

        paste = ''.join(user_input)

        ids = clean_up(paste)

        print(ids)
        print("MADE IT TO IDS\n")
        
        ids_for_usernames(ids)


        save_to_file() 

        print(idlist)



        window['-INPUT-']('')



window.close()