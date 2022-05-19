import os
import PySimpleGUI as sg

def save_to_file(content):
    with open("USERNAMES.txt", "a") as file:
        file.write(content + '\n')
        print(f"File edited with {content}.")

def read_file_back():
    with open('USERNAMES.txt', 'r') as file:
        print(file.read())



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

        save_to_file(paste)

        read_file_back()

        window['-INPUT-']('')



window.close()