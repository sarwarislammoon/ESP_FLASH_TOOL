
from tkinter import *
from tkinter import filedialog
from tkinter import filedialog,messagebox
import os


root = Tk() 
root.geometry("300x130")
root.resizable(0,0)
root.title('ESP FW Loader 0.0.1')



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
    global filepath
    PORT_Adress=PORT.get()
    device=chPORT.get(ACTIVE)

    print("Param") 
    print(filepath)
    print(PORT_Adress)
    print(device)

    os.system('esptool.py erase_flash')

    if device =="ESP8266" :  
        if PORT_Adress == '':
            os.system('python tools/esptool/esptool.py --baud 115200 --after hard_reset --chip esp8266 write_flash 0x0 %s ' % (filepath))
        else:
            os.system('python tools/esptool/esptool.py --port %s --baud 115200 --after hard_reset --chip esp8266 write_flash 0x0 %s ' % (PORT_Adress,filepath))
    elif device =="ESP32":
        if PORT_Adress == "":
            os.system( 'python tools/esptool/esptool.py  --baud 921600 --after hard_reset --before default_reset --chip esp32 write_flash -z --flash_mode dio --flash_freq 80m --flash_size detect 0xe000 tools/boot_app0.bin 0x1000 tools/bootloader_qio_80m.bin 0x10000 %s 0x8000 tools/default.bin '% (filepath))
        else:
            os.system( 'python tools/esptool/esptool.py --port %s --baud 921600 --after hard_reset --before default_reset --chip esp32 write_flash -z --flash_mode dio --flash_freq 80m --flash_size detect 0xe000 tools/boot_app0.bin 0x1000 tools/bootloader_qio_80m.bin 0x10000 %s 0x8000 tools/default.bin '% (PORT_Adress,filepath))
    else:
        pass



chPORTLabel = LabelFrame(root, text="Device", padx=5, pady=5)
chPORTLabel.pack()

chPORT = Listbox(chPORTLabel,width=20,height=2) 
chPORT.insert(0, 'ESP32') 
chPORT.insert(1, 'ESP8266')  
chPORT.pack()   

chPORTLabel.place(x=5,y=0)

PORTLabel=LabelFrame(root, text="PORT", padx=5, pady=5)
PORTLabel.pack()
PORT = Entry(PORTLabel)
PORT.pack()

PORTLabel.place(x=150,y=0)



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