# EXPY SEA-CLAM

import webbrowser
import psutil
import mouse
import platform
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from pywinauto import Application
from tkinter import filedialog
import pyautogui
from tkinter import *
import tkinter as tk
import keyboard
import os
from time import sleep

try:
    if os.name == 'nt':
        print("os")
except ModuleNotFoundError:
    print("Exception when importing modules")
    print("Installing necessary modules....")
    if os.path.isfile("requirements.txt"):
        os.system("pip install -r requirements.txt")
    else:
        os.system("pip install keyboard")
        os.system("pip install pyautogui")
        os.system("pip install pywinauto")
        os.system("pip install mouse")
        os.system("pip install psutil")
        os.system("pip install tkinter")
    sleep(1.5)
    os._exit(1)


process = None
ProcBOX = None
StatusBOX = None 
CodeBOX = None
OutBOX = None

old = None

read = False

scrparent = os.path.abspath(__file__)
parent = os.path.dirname(scrparent)

def print(txt):
    t = OutBox.get("1.0", "end-1c")
    OutBox.insert(END,txt)

def load():
    global old
    old = CodeBOX.get("1.0", tk.END)
    path=filedialog.askopenfilename(title="Select a file", filetypes=(("Expy Scripts", "*.expy"),))
    with open(path, 'r') as file:
        content = file.read()
        print("loaded:" + file.name)    
    CodeBOX.delete("1.0", tk.END)    
    CodeBOX.insert("insert", content)
def save():
    data = CodeBOX.get("1.0", tk.END)
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Expy Scripts", "*.expy"), ("All files", "*.*")))
    with open(path, 'w') as file:
     file.write(data)

def WIND_DOUBLE_CLICK(type):
    for i in range(2):
        sleep(0.01)
        mouse.click(type)

def KEY_HOLD(key, time):
    process.activate()
    print("pressed key: "+key)
    keyboard.press(key)
    sleep(time)
    keyboard.release(key)

def FUNC_RESET():
    process.activate()
    print("reset")
    keyboard.press("esc")
    sleep(0.25)
    keyboard.release("esc")
    keyboard.press("r")  
    sleep(0.25)
    keyboard.release("r")
    keyboard.press("enter")
    sleep(0.25)
    keyboard.release("enter")

def KEY_PRESS(key):
    process.activate()
    print("pressed key: "+key)
    keyboard.press(key)
    sleep(0.01)
    keyboard.release(key)   

def KEY_REPEAT(key, repeated, speed):
    process.activate()
    for i in range(repeated):
        keyboard.press(key)
        sleep(speed)
        keyboard.release(key)
        sleep(speed)

def WIND_CLICK(type):
    process.activate()
    mouse.click(button=type)

def WIND_HOLD_CLICK(type, length):
    process.activate()
    mouse.hold(type)
    sleep(length)
    mouse.release(type)

def WIND_MOVE(y,x,abso,dur):
    process.activate()
    val = False
    if abso == "yes":
        val = True
    mouse.move(x, y, absolute=val, duration=int(dur))

def FUNC_CHAT(message):
     process.activate()
     keyboard.send("/")
     sleep(0.3)
     keyboard.write(message)
     sleep(0.2)
     keyboard.press("enter")
     sleep(0.3)
     keyboard.release("enter")

def MOVE_JUMP():
    KEY_HOLD("space",0.5)

def UI_LEAVE():
    process.activate()
    print("leave")
    keyboard.press("esc")
    sleep(0.25)
    keyboard.release("esc")
    keyboard.press("l")  
    sleep(0.25)
    keyboard.release("l")
    keyboard.press("enter")
    sleep(0.25)
    keyboard.release("enter")
  

def syntax(times, loop):
   global read
   if process == None:
       messagebox.showerror("expy", "Connect to an application first!")
       return
   for i in range(times): 
    EXE = CodeBOX.get("1.0", tk.END)
    EXES = EXE.split()
    if keyboard.is_pressed('ctrl+f'):
        break
    for syn in EXES:
        if 'holdkey' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1].split(")")[0]
                if loop == False:
                    if float(a2) < 0.01:
                       if read == False:
                        ans=messagebox.askquestion("Continue?", "Values lower than 0.01 can cause crashing, softlocking and unstableness, especially with loop(). Would you still like to run your code?")
                        while True:
                         if ans == "yes":
                          read = False
                          break
                         elif ans == "no":
                          read = False
                          break
                        if ans == "no":
                            return 
                KEY_HOLD(str(a1), float(a2))
            else:
                next 
        if 'mousehold' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1].split(")")[0]
                WIND_HOLD_CLICK(a1, float(a2))
            else:
                next  
        if 'mousemove' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1]
                a3 = undersplit[2]
                a4 = undersplit[3].split(")")[0]
                WIND_MOVE(a1,a2,a3,a4)
            else:
                next                 
        if 'presskey' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0].split(")")[0]
                KEY_PRESS(str(a1))
            else:
                next

        if 'pause' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split(")")
                sleep(float(undersplit[0]))
            else:
                next   
        if 'reset()' in syn:
            FUNC_RESET()
            next  
        if 'jump()' in syn:
            MOVE_JUMP()
            next      
        if 'repeatkey' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1]
                a3 = undersplit[2].split(")")[0]
                KEY_REPEAT(str(a1), int(a2), float(a3))
            else:
                next               
        if 'chat' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split(")")
                message = ""
                if undersplit[0].find("_"):
                    space = undersplit[0].split("_")
                    for wo in space:
                     message = message + " " + wo
                else:
                    message = undersplit      
                FUNC_CHAT(message)
            else:
                next      
        if 'click' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split(")")
                WIND_CLICK(undersplit[0])
            else:
                next  
        if 'doubleclick' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split(")")
                WIND_DOUBLE_CLICK(undersplit[0])
            else:
                next               
        if 'loop' in syn and loop == False:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split(")")
                syntax(int(undersplit[0]),True)
            else:
                next   


def launch():
     syntax(1,False)

def attach(exe_name): 
    if platform.system() == "Windows":
     if float(platform.release()):
         if float(platform.release()) < 7:
           print("UNSUPPORTED OS: " + platform.release())
           messagebox.showerror("Fatal Error", "expy doesn't support your operating system. Visit the github for instructions.")     
           return  
     else:
         if platform.release() == "XP" or platform.release() == "Vista":
           print("UNSUPPORTED OS: " + platform.release())
           messagebox.showerror("Fatal Error", "expy doesn't support your operating system. Visit the github for instructions.")     
           return   
     global process
     exe_name = exe_name + ".exe"
     for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == exe_name:
            pid = proc.info['pid']
            app = Application().connect(process=pid)
            process = pyautogui.getWindowsWithTitle(app.windows()[0].window_text())[0]
            return app.windows()[0].window_text()
        else:
            process = None
    else:
           print("UNSUPPORTED OS: " + platform.system())
           messagebox.showerror("Fatal Error", "expy doesn't support your operating system. Visit the github for instructions.")     
    return None

def clear():
 global old
 old = CodeBOX.get("1.0", tk.END)
 CodeBOX.delete("1.0", tk.END)
def restore():
  CodeBOX.delete("1.0", tk.END)
  CodeBOX.insert("insert",old) 


def on_attach_button():
    att = attach(ProcBOX.get())
    if att != None:
        print("Connected.")
        StatusBOX.config(text="Status: Connected")
    else:
        print("Unable to connect.")
        messagebox.showerror("expy", "Unable to connect.")
        StatusBOX.config(text="Status: Disconnected")

def openraw():
 webbrowser.open('https://raw.githubusercontent.com/twigkid/expy/main/README.md')
def open():
 webbrowser.open('https://github.com/twigkid/expy') 


Core = tk.Tk()
Core.geometry("550x350")
Core.title("Ex-PY Clam V2.1.0")

Core.resizable(width=False, height=False)
Core.attributes("-topmost", 1)

ProcessBox = tk.Entry()
ProcessBox.place(x = 360, y = 323)
ProcBOX = ProcessBox

Attach = tk.Button(text = "Connect", command = on_attach_button)
Attach.config(height = 1)
Attach.place(x = 490, y = 320)

Status = tk.Label(Core, text = "Status: Disconnected")
Status.place(x=185,y=322)
StatusBOX = Status

MainBox = ScrolledText(Core)
MainBox.place(x = 15, y = 60, width=356, height=250)
CodeBOX = MainBox


OutBox = ScrolledText(Core)
OutBox.place(x = 381, y = 60, width=164, height=250)

OutBOX = OutBox

Execute = tk.Button(text="Launch",command=launch)
Execute.place(x=15, y = 320)

Clear = tk.Button(text="Clear",command=clear)
Clear.place(x=75, y = 320)

Restore = tk.Button(text="Restore",command=restore)
Restore.place(x=120, y = 320)

Bar = tk.Menu(Core)
menua=tk.Menu(Bar,tearoff=0)
menua.add_command(label="Save", command=save)
menua.add_command(label="Load",command=load)
menua.add_command(label="Exit",command=Core.destroy)
Bar.add_cascade(label="File", menu=menua)

AAA = tk.Menu(Bar,tearoff=0)

AAA.add_command(label="Github",command=open)
AAA.add_command(label="Github (Raw)",command=openraw)
Bar.add_cascade(label="Help", menu=AAA)

Core.config(menu=Bar)

Core.mainloop()
