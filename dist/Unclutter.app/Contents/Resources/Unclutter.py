import tkinter
import os
import shutil
from tkinter import *
FlexyPath2 = os.path.dirname(os.path.abspath(__file__))

FlexyPath = os.path.expanduser('~')
computerName = FlexyPath

print(computerName)
os.chdir(computerName +"/Downloads")

dic = []
for line in os.listdir(): 
    dic.append(line)


os.chdir("/Applications")
appDic = []
for line1 in os.listdir(): 
    appDic.append(line1)

print(dic)

def createFolder(directory, name):
    try:
        if not os.path.exists(directory):
            [os.mkdir(os.path.join(computerName + directory, name))]
    except:
        print ('Error: Creating directory. ' +  name)

def fileSystem():
    createFolder("/desktop", "School Work")
    createFolder("/desktop/School Work", "Maths")
    createFolder("/desktop/School Work", "English")
    createFolder("/desktop/School Work", "Science")
    createFolder("/desktop/School Work/Science", "Physics")
    createFolder("/desktop/School Work/Science", "Chemistry")
    createFolder("/desktop/School Work", "Geography")
    createFolder("/desktop/School Work", "History")
    createFolder("/desktop/School Work", "SDD")
    createFolder("/desktop/School Work", "Christian Studies")
    createFolder("/desktop/School Work", "PDHPE")
    createFolder("/desktop/School Work", "Images")
    createFolder("/desktop/School Work", "Notifications")
    createFolder("/desktop/School Work", "Economics")
    createFolder("/desktop/School Work", "Religion")
    createFolder("/desktop", "My Stuff")
    createFolder("/desktop/My Stuff", "DMG")
    createFolder("/desktop/My Stuff", "ZIP")
    createFolder("/desktop/My Stuff", "Audio")
    createFolder("/desktop/My Stuff", "Videos")


    


def CleanEND(extensions, place):
    global dic
    dic = []
    for line in os.listdir():
        line = line.lower()
        dic.append(line)
    exts = tuple(extensions)

    dmga = [f for f in dic if f.endswith(exts)]

    dmgal = len(dmga)
    var = 0
    while dmgal != var:
        listbox.insert(END, dmga[(var)])
        shutil.move(computerName +'/downloads/' + dmga[(var)], place + dmga[var])
        var = var + 1
        
    print(dmga)
    
    os.chdir(computerName +"/Downloads")


def Clean(extensions, place):
    global dic
    dic = []
    for line in os.listdir():
        line = line.lower()
        dic.append(line)


    dicl = len(dic)
    var = 0
    while dicl != var:
        if extensions in dic[var]:
            print(dic[var])
            listbox.insert(END, dic[(var)])
            shutil.move(computerName +'/downloads/' + dic[(var)], place + dic[var])
        var = var + 1

    os.chdir(computerName +"/Downloads")


window = tkinter.Tk()
window.minsize(450, 210)
window.title("Unclutter")

listbox = Listbox(window) 

listbox.pack(side = LEFT, fill = BOTH) 

scrollbar = Scrollbar(window) 
 
scrollbar.pack(side = RIGHT, fill = BOTH) 

listbox.config(yscrollcommand = scrollbar.set) 
 
scrollbar.config(command = listbox.yview) 
listbox.place(x=250, y=30)

label = tkinter.Label(window, text="Press Button To Unclutter")
label2 = tkinter.Label(window, text="Press Button To Create Folders")
label3 = tkinter.Label(window, text="Files Moved")

label.place(x=10, y=10)
label2.place(x=10, y=70)
label3.place(x=295, y=5)

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

center(window)
counter = 0



def press():
    print("pressed")
    Clean("maths", computerName +"/Desktop/School Work/Maths/")
    Clean("outcomes", computerName +"/Desktop/School Work/Science/")
    Clean("year 11", computerName +"/Desktop/School Work/Notifications/")
    Clean("y11", computerName +"/Desktop/School Work/Notifications/")
    Clean("software", computerName +"/Desktop/School Work/SDD/")
    Clean("sdd", computerName +"/Desktop/School Work/SDD/")
    Clean("programming", computerName +"/Desktop/School Work/SDD/")
    Clean("religion", computerName +"/Desktop/School Work/Religion/")
    Clean("economics", computerName +"/Desktop/School Work/Year 11/Economics/")
    Clean("stage 6", computerName +"/Desktop/School Work/Notifications/")
    Clean("s6", computerName +"/Desktop/School Work/Notifications/")
    Clean("english", computerName +"/Desktop/School Work/English/")
    Clean("macbeth", computerName +"/Desktop/School Work/English/")
    Clean("geography", computerName +"/Desktop/School Work/Geography/")
    Clean("history", computerName +"/Desktop/School Work/History/")
    Clean("physics", computerName +"/Desktop/School Work/Science/Physics/")
    Clean("chemistry", computerName +"/Desktop/School Work/Science/Chemistry/")
    Clean("dt", computerName +"/Desktop/School Work/DT/")
    Clean("python", computerName +"/Desktop/School Work/SDD/")
    Clean("pip", computerName +"/Desktop/School Work/SDD/")
    
    
    CleanEND(['.py'], computerName +"/Desktop/School Work/SDD/")
    CleanEND(['.mp3'], computerName +"/Desktop/MY STUFF/Audio/")
    CleanEND(['.dmg'], computerName +"/Desktop/MY STUFF/DMG/")
    CleanEND(['.mp4', '.mov'], computerName +"/Desktop/MY STUFF/Videos/")
    CleanEND(['.zip'], computerName +"/Desktop/MY STUFF/ZIP/")
    CleanEND(['.ai'], computerName +"/Desktop/School Work Work/DT/")
    CleanEND(['.png', '.jpg', '.jpeg'], computerName +"/Desktop/School Work/Images/")
    CleanEND(['.gcode', '.stl'], computerName +"/Desktop/3D Printer/")
    CleanEND(['.app'], "/Applications/")


button = tkinter.Button(window, text="Button", command=press)
button2 = tkinter.Button(window, text="Button", command=fileSystem)
button.place(x=10, y=40)
button2.place(x=10, y=100)

window.mainloop()