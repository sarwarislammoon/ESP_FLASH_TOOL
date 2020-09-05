from tkinter import *
from tkinter import filedialog
from tkinter import filedialog,messagebox
from MQTT.mqttListener import *
from globalVar import *
import os



def openFile():
    global filepath
    filepath = StringVar()
    #Fetch the file path of the hex file browsed.
    if(filepath == ""):
        filepath = filedialog.askopenfilename( initialdir = os.getcwd() ,
            title = "select a file", filetypes = [("bin files", "*.bin")])
    else:
        filepath = filedialog.askopenfilename( initialdir=filepath,
            title = "select a file", filetypes = [("bin files", "*.bin")])
    
    if filepath == "":
            #filepathlabel.config(text="Open bin file")
            filepathlabel.insert(index=0,String=None)
    else:
            #filepathlabel.config(text=filepath)
            filepathlabel.insert(index=0,string=filepath)
    

def loadFW():
    print(lastMsg[1])
    '''
    global filepath
    IP_Adress=IP.get()
    device=chip.get(ACTIVE)

    print("Param") 
    print(filepath)
    print(IP_Adress)
    print(device)

    if device =="ESP8266" :
        os.system('python tools/esp8266ota.py -r -d -i %s -p 8266 --auth= -f %s' % (IP_Adress,filepath))
    elif device =="ESP32":
        os.system('python tools/esp32ota.py -r -d -i %s -p 3232 --auth= -f %s' %(IP_Adress,filepath))
    else:
        pass
    '''






root = Tk() 
root.geometry("300x130")
root.resizable(0,0)
root.title('ESP OTA Loader 0.0.2')


chipLabel = LabelFrame(root, text="Device", padx=5, pady=5)
chipLabel.pack()

chip = Listbox(chipLabel,width=20,height=2) 
chip.insert(0, 'ESP32') 
chip.insert(1, 'ESP8266')  
chip.pack()   

chipLabel.place(x=5,y=0)

IPLabel=LabelFrame(root, text="IP", padx=5, pady=5)
IPLabel.pack()
IP = Entry(IPLabel)
IP.pack()

IPLabel.place(x=150,y=0)



filrbrowsButton=Button(root, text="Open files", command=openFile,height=1,width=8)
filrbrowsButton.pack()
filrbrowsButton.place(x=5,y=100)
#filepathlabel = Label(root,text = "Open bin file",padx=5,pady=5)
filepathlabel =Entry(root,width=30)
filepathlabel.pack()
filepathlabel.place(x=100,y=100)
loadButton=Button(root, text="Load", command=loadFW,height=1,width=8)
loadButton.pack()
loadButton.place(x=5,y=70)

root.mainloop() 