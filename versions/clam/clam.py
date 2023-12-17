# EXPY SEA-CLAM

import sys
from io import StringIO
import psutil
import mouse
from tkinter.scrolledtext import ScrolledText
from pywinauto import Application
from tkinter import filedialog
import pyautogui
from tkinter import *
import tkinter as tk
import keyboard
import os
from time import sleep

process = None
ProcBOX = None
StatusBOX = None 
CodeBOX = None
OutBOX = None

scrparent = os.path.abspath(__file__)
parent = os.path.dirname(scrparent)

def print(txt):
    t = OutBox.get("1.0", "end-1c")
    OutBox.insert(END,txt)

class onlog:
    def writeto(self, s):
        OutBOX.insert(tk.END, s)
        OutBOX.see(tk.END)

def load():
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

def KEY_HOLD(key, time):
    process.activate()
    print("pressed key: "+key)
    keyboard.press(key)
    sleep(time)
    keyboard.release(key)

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

def FUNC_CHAT(message):
     process.activate()
     keyboard.send("/")
     sleep(0.3)
     keyboard.write(message)
     sleep(0.2)
     keyboard.press("enter")
     sleep(0.3)
     keyboard.release("enter")



def launch():
    EXE = CodeBOX.get("1.0", tk.END)
    EXES = EXE.split()
    for syn in EXES:
        if 'holdkey' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1].split(")")[0]
                KEY_HOLD(str(a1), float(a2))
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
def attach(exe_name):
    global process
    exe_name = exe_name + ".exe"
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == exe_name:
            pid = proc.info['pid']
            app = Application().connect(process=pid)
            process = pyautogui.getWindowsWithTitle(app.windows()[0].window_text())[0]
            return app.windows()[0].window_text()
    return None

def clear():
 CodeBOX.delete("1.0", tk.END)

def on_attach_button():
    att = attach(ProcBOX.get())
    if att != None:
        print("Attached.")
        StatusBOX.config(text="Status: Connected")
    else:
        print("Unable to attach.")
        StatusBOX.config(text="Status: Disconnected")


Core = tk.Tk()
Core.geometry("550x350")
Core.title("Ex-PY Clam")

Core.resizable(width=False, height=False)
Core.attributes("-topmost", 1)

ProcessBox = tk.Entry()
ProcessBox.place(x = 360, y = 323)
ProcBOX = ProcessBox

Attach = tk.Button(text = "Connect", command = on_attach_button)
Attach.config(height = 1)
Attach.place(x = 490, y = 320)

Status = tk.Label(Core, text = "Status: Disconnected")
Status.place(x=425,y=25)
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

Bar = tk.Menu(Core)
menua=tk.Menu(Bar,tearoff=0)
menua.add_command(label="Save", command=save)
menua.add_command(label="Load",command=load)
menua.add_command(label="Exit",command=Core.destroy)
Bar.add_cascade(label="File", menu=menua)

Core.config(menu=Bar)

Core.mainloop()
