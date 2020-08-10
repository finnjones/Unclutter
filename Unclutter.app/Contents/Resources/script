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

print(appDic)
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
    createFolder("/desktop/School Work", "Geography")
    createFolder("/desktop/School Work", "History")
    createFolder("/desktop/School Work", "Christian Studies")
    createFolder("/desktop/School Work", "PDHPE")
    createFolder("/desktop/School Work", "Images")
    createFolder("/desktop/School Work", "Notifications")
    createFolder("/desktop", "My Stuff")
    createFolder("/desktop/My Stuff", "DMG")
    createFolder("/desktop/My Stuff", "ZIP")
    createFolder("/desktop/My Stuff", "Audio")

    


    

# def CleanENDApp(extensions, place):

#     dicl = len(dic)
#     var = 0
#     while dicl != var:
#         if extensions in dic[var]:
#             print(dic[var])
#             shutil.move(computerName +'/downloads/' + dic[(var)], place + dic[var])
#         var = var + 1

    
#     exts = tuple(extensions)

#     dmga = [f for f in dic if f.endswith(exts)]

#     dmgal = len(dmga)
#     var = 0
#     while dmgal != var:
        
#         shutil.move(computerName +'/downloads/' + dmga[(var)], place + dmga[var])
#         var = var + 1
        
#     print(dmga)


# def Cl():
#     sdic = []
#     dicl = len(appDic)
#     var = 0
#     while dicl != var:
#         appDic[var] = ''.join(appDic[var].split())[:-4]
#         print(appDic[var])
#         sdic.append(appDic[var])
#         var = var + 1

#     varl = 0
#     for f in dic:
#         # print(f)
#         varl = varl + 1
#         # print(f)
        
#         # print(sdic[varl])
#         # print("------------------------------------------------------------------------")

#         for sdic in f:
#             print("good")
#             print(sdic)
#         # if sdic[varl] in f:
#         #     print('asd')
#         #     print(sdic[varl])

#         # exts = tuple(".dmg")

#         # dmga = [f for f in dic if f.endswith(exts)]

#         # dmgal = len(dmga)
#         # var1 = 0
#         # while dmgal != var1:
#         #     print("hello")
#         #     var1 = var1 + 1
        
#     # print(dmga)



def CleanEND(extensions, place):
    exts = tuple(extensions)

    dmga = [f for f in dic if f.endswith(exts)]

    dmgal = len(dmga)
    var = 0
    while dmgal != var:
        
        shutil.move(computerName +'/downloads/' + dmga[(var)], place + dmga[var])
        var = var + 1
        
    print(dmga)

def Clean(extensions, place):
    


    dicl = len(dic)
    var = 0
    while dicl != var:
        if extensions in dic[var]:
            print(dic[var])
            shutil.move(computerName +'/downloads/' + dic[(var)], place + dic[var])
        var = var + 1
# Initialize the main window
window = tkinter.Tk()
# Size windows to 400 x 400px
window.minsize(400, 400)
# Give your window a title
window.title("Unclutter")
# Set Icon
# window.wm_iconbitmap("AppIcon.icns")

 
# Place 'Hello World' label on the window
label = tkinter.Label(window, text="Press Button To Unclutter")
label2 = tkinter.Label(window, text="Press Button To Set Up File System")
# Place label at coordinates x=10 and y=10 (top right hand corner)
label.place(x=10, y=10)
label2.place(x=10, y=70)
 
 
# Function to find the screen dimensions, calculate the center and set geometry
def center(win):
    # Call all pending idle tasks - carry out geometry management and redraw widgets.
    win.update_idletasks()
    # Get width and height of the screen
    width = win.winfo_width()
    height = win.winfo_height()
    # Calculate geometry
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    # Set geometry
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
 
 
# Center Window on Screen
center(window)
 
# Initialize counter
counter = 0
 
# Define button press function
def press():
    # use globally set counter variable
    print("pressed")



    Clean("Maths", computerName +"/Desktop/School Work/Maths/")
    Clean("Outcomes", computerName +"/Desktop/School Work/Science/")
    Clean("Year 10", computerName +"/Desktop/School Work/Notifications/")
    Clean("English", computerName +"/Desktop/School Work/English/")
    Clean("Macbeth", computerName +"/Desktop/School Work/English/")
    Clean("Geography", computerName +"/Desktop/School Work/Geography/")
    Clean("History", computerName +"/Desktop/School Work/History/")

    Clean("REDEMPTION", computerName +"/Desktop/School Work/English/")



    Clean("DT", computerName +"/Desktop/School Work/DT/")
    Clean("python", computerName +"/Desktop/School Work/Information Software Technology/")
    Clean("pip", computerName +"/Desktop/School Work/Information Software Technology/")
    
    CleanEND(['.mp3'], computerName +"/Desktop/MY STUFF/Audio/")
    CleanEND(['.dmg'], computerName +"/Desktop/MY STUFF/DMG/")
    CleanEND(['.zip'], computerName +"/Desktop/MY STUFF/ZIP/")
    CleanEND(['.ai'], computerName +"/Desktop/School Work Work/DT/")
    CleanEND(['.png', '.jpg', '.jpeg', '.JPG'], computerName +"/Desktop/School Work/Images/")
    CleanEND(['.gcode', '.stl'], computerName +"/Desktop/3D Printer/")
    CleanEND(['.py'], computerName +"/Desktop/School Work/IST/")

    CleanEND(['.app'], "/Applications/")



# Place 'Change Label' button on the window
button = tkinter.Button(window, text="Button", command=press)
button2 = tkinter.Button(window, text="Button", command=fileSystem)
# Place label at coordinates x=10 and y=10 (top right hand corner)
button.place(x=10, y=40)
button2.place(x=10, y=100)
# w.place(x=10, y=150)
# Show new window
window.mainloop()