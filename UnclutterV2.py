import os
import shutil
computerName = ""
f= open("das.txt","w")
f.write('bra')
f.close()
computerName = 'finn.jones'
# app = contents[1]
app = 'y'
if app == "n":
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop", "School Work"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/School Work", "Maths"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/School Work", "English"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/School Work", "Science"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/School Work", "Geography"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/School Work", "History"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/School Work", "Christian Studies"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/School Work", "PDHPE"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/School Work", "Images"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop", "My Stuff"))]
    [os.mkdir(os.path.join("/Users/"+ computerName +"/desktop/My Stuff", "DMG"))]


os.chdir("/Users/"+ computerName +"/Downloads")
dic = []
for line in os.listdir(): 
    dic.append(line)

os.chdir("/Applications")
appDic = []
for line1 in os.listdir(): 
    appDic.append(line1)

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        


def CleanEND(extensions, place):
    exts = tuple(extensions)

    dmga = [f for f in dic if f.endswith(exts)]

    dmgal = len(dmga)
    var = 0
    while dmgal != var:
        
        shutil.move('/Users/'+ computerName +'/downloads/' + dmga[(var)], place + dmga[var])
        var = var + 1
        
    print(dmga)

def Clean(extensions, place):
    


    dicl = len(dic)
    var = 0
    while dicl != var:
        if extensions in dic[var]:
            print(dic[var])
            shutil.move('/Users/'+ computerName +'/downloads/' + dic[(var)], place + dic[var])
        var = var + 1
    # print(dic)

def deleteApp():
    exts = tuple(['.dmg'])

    dmga = [f for f in dic if f.endswith(exts)]

    dmgal = len(dmga)
    var = 0
    while dic != var:
        dmgall = dmgal[var]
        print
        print(dmgall)
        print(dmgall[:-1])
        # if dmgal[:-1] in appDic:
        #     print("yes")
        var = var + 1
    
    print(dmga)

# deleteApp()
Clean("Maths", "/Users/"+ computerName +"/Desktop/School Work/Maths/")
Clean("Outcomes", "/Users/"+ computerName +"/Desktop/School Work/Science/")
Clean("Year 10", "/Users/"+ computerName +"/Desktop/School Work/Notifications/")
Clean("English", "/Users/"+ computerName +"/Desktop/School Work/English/")
Clean("Geography", "/Users/"+ computerName +"/Desktop/School Work/Geography/")
Clean("History", "/Users/"+ computerName +"/Desktop/School Work/History/")

Clean("REDEMPTION", "/Users/"+ computerName +"/Desktop/School Work/English/")
# print(appDic)


Clean("DT", "/Users/"+ computerName +"/Desktop/School Work/DT/")
Clean("python", "/Users/"+ computerName +"/Desktop/School Work/Information Software Technology/")
Clean("pip", "/Users/"+ computerName +"/Desktop/School Work/Information Software Technology/")

CleanEND(['.dmg'], "/Users/"+ computerName +"/Desktop/MY STUFF/DMG/")
# CleanEND(['.ai'], "/Users/"+ computerName +"/Desktop/School Work Work/DT/")
CleanEND(['.png', '.jpg', '.jpeg', '.JPG'], "/Users/"+ computerName +"/Desktop/School Work/Images/")



CleanEND(['.app'], "/Users/"+ computerName +"/Applications/")

