import os
import bot_module as module

Windows_user = os.getlogin()



def backup():
    path = os.getcwd()
    backup = f"{path}\\Backup_chatlogs\\"
    source = f"C:\\Users\\{Windows_user}\\AppData\\LocalLow\\RoarkInc\\raot\\chatlogs\\history\\"
    
    allfiles = os.listdir(source)
    
    print(f"Current number of chatlog files = {len(allfiles)}")

    for f in allfiles:
        os.rename((source + f), (backup + f))


def update_history():
    """Gets the chatlog history if user has enabled logging""" 

    #placeholders
    data = list()

    #finds chatlogs with windows username
    history = rf"C:\Users\{Windows_user}\AppData\LocalLow\RoarkInc\raot\chatlogs\history"

    for filename in os.listdir(history):
    #this one is fine... Don't touch it
        with open(f"{history}\{filename}", 'r', encoding="utf8") as old_chatlog:
            #reading chatlog\history files and saving data as chatlog >_> I'm lazy with names
            _chatlog = old_chatlog.readlines()
            
            for lns in _chatlog:
                if lns.startswith('User'):
                    data.append(lns)

            for ln in data:
                #Clean up lines
                ln = ln.replace('Username: ', '')
                ln = ln.replace(' Id: ', '')
                ln = ln.replace('\n', '')
                ln = ln.replace(' ', '')
                items = ln.split('|')
                items.reverse()

                _id = items[0::2]
                _name = items[1::2]



                items = module.merge(_id, _name)

                module.write_name_storage(items)
    
    #backup to end the function
    backup()         
    
def get_current_chatlog():
    """Gets the chatlog if user has enabled logging""" 
    try:
        #placeholders
        data = list()

        #finds chatlogs with windows username
        chatlog = rf"C:\Users\{Windows_user}\AppData\LocalLow\RoarkInc\raot\chatlogs"

        #this one is fine... Don't touch it
        with open(f"{chatlog}\chatlog.txt", 'r', encoding="utf8") as file:
            #reading chatlog\history files and saving data as chatlog >_> I'm lazy with names
            file = file.readlines()
            
            for lns in file:
                if lns.startswith('User'):
                    data.append(lns)

            for ln in data:
                #Clean up lines
                ln = ln.replace('Username: ', '')
                ln = ln.replace(' Id: ', '')
                ln = ln.replace('\n', '')
                ln = ln.replace(' ', '')
                items = ln.split('|')
                items.reverse()

                _id = items[0::2]
                _name = items[1::2]



                items = module.merge(_id, _name)

                module.write_name_storage(items)
    #we get exceptions if the file doesn't exist so we stopping that
    except Exception as e: print(e)

