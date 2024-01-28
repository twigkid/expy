# Ex-PY V2.2.0
import os
import sys
from time import sleep
ver="2.2.0"
os.system("clear")
print("\033[92mWelcome to Ex-PY Linux " + str(ver) + "!")
print("If you encounter any errors, glitchs or bugs. Please report them at: https://discord.gg/YjGtc36W53")
print("If this is your first time using V2.2.0 then, Please type Install.")


iconmode = False

def checkcon():
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

def reboot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
def checkversion():
        http = requests.get(url="https://pastebin.com/raw/csExAqQ1")
        if http.text!=ver:
            print("\033[91mEx-PY is out of date! Update it at: https://github.com/twigkid/expy")
            sleep(0.25)
        else:
            print("\033[95mEx-PY is up to date.")   

def icon():
    print("EX-PY Linux V1 Doesn't support icons. Moving on...")

user_input = input("\033[92mHow would you like to run Ex-PY? (install/launch/exit/quickinstall/info/enter): ")
if user_input.lower() == "install":
    print("Launching Ex-PY Installer...")
    sleep(0.5)
    os.system("pip3 install requests")
    os.system("pip3 install sockets")
    os.system("clear")
    print('''
  ______             _______     __
 |  ____|           |  __ \ \   / /
 | |__  __  ________| |__) \ \_/ / 
 |  __| \ \/ /______|  ___/ \   /  
 | |____ >  <       | |      | |   
 |______/_/\_\      |_|      |_| v2.2.0
      Made by twigkid, Idea by: blatant
       2023 - 2024 Ex-PY
          Report Errors at: https://discord.gg/YjGtc36W53
        https://github.com/twigkid/expy     
                                
      ''')

    import socket
    import requests
    #https://pastebin.com/raw/csExAqQ1 this is the version link lol
    
    checkversion()

    print("\033[96mEx-PY V2.2.0 Linux (Clam) Build: 1.0.0")
    sleep(0.5)

    icon()

    user_input = input("Do you want to download all Packages? (yes/no): ")
    if user_input.lower() == "yes" or user_input.lower() == "y":
        print("\033[96mThis may take a-while depending on write & internet speeds.")
        sleep(0.45)
        print("\033[92mStarting Downloads.")
        if checkcon() == True:
             os.system("pip3 install pyautogui")
             os.system("pip3 install pywinauto")
             os.system("pip3 install mouse")
             os.system("pip3 install pygame")
             os.system("pip3 install psutil")
        else:
            print("\033[91mAn Internet Connection Isn't present. Ex-PY Will still function but updates or fixes won't be present.")
    print("\033[92mFinished, Launching Ex-PY.")
    sleep(0.5)    
    if user_input.lower() == "exit":
     os._exit(1)     
    
elif user_input.lower() == "info":
    print('''
          V2.2.0
          By twigkid, Idea by Blatant
          Launch: Doesn't install anything, Just opens Ex-PY.
          Install: Installs all modules & packages for Ex-PY And Launches.
          QuickInstall: Installs all modules & packages without any pauses And Launches.
          Enter Key: Launches Ex-PY with every default.
          Info: Opens this menu
          ''')
    if "y" in input("Done (y): ").lower():      
     user_input=None
     reboot(False)
elif user_input.lower() == "launch":
    icon()
    sleep(1)    
    print("\033[92mLaunching")
    sleep(0.25) 
elif user_input.lower() == "exit":
    os._exit(1)    
if user_input.lower() == "quickinstall":
    os.system("pip3 install requests")
    os.system("pip3 install sockets")
    os.system("clear")
    import socket
    import requests
    def checkversion():
        http = requests.get(url="https://pastebin.com/raw/csExAqQ1")
        if http.text!=ver:
            print("\033[91mEx-PY is out of date! Update it at: https://github.com/twigkid/expy")
        else:
            print("\033[95mEx-PY is up to date.")    
    checkversion()
    print("\033[96mEx-PY V2.2.0 (Clam) Build: 1.0.0")
    if checkcon() == True:
        os.system("pip3 install pyautogui")
        os.system("pip3 install pywinauto")
        os.system("pip3 install mouse")
        os.system("pip3 install pygame")
        os.system("pip3 install psutil")
    else:
         print("\033[91mAn Internet Connection Isn't present. Ex-PY Will still function but updates or fixes won't be present.")
    icon()
    print("\033[92mFinished, Launching Ex-PY.") 



import webbrowser
import psutil
import mouse
import pyautogui
import tkinter as tk
import pygame
from random import randrange
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import *
from random import randrange

os.system("clear")
print('''\033[95m
      
d88888b db    db        d8888b. db    db 
88'     `8b  d8'        88  `8D `8b  d8' 
88ooooo  `8bd8'         88oodD'  `8bd8'  
88~~~~~  .dPYb.  C8888D 88~~~      88    
88.     .8P  Y8.        88         88    
Y88888P YP    YP        88         YP   
       
    V2.2.0 By twigkid, 2024
      Idea by Blatant,
        Errors 'n stuff will appear below.
      ''')


cprint = print

StatusBOX = None 
CodeBOX = None
OutBOX = None
read = False
core = None
read = False


def print(txt):
    t = OutBox.get("1.0", "end-1c")
    OutBox.insert(END,txt)


def about(): 
    messagebox.showinfo(title="About", message='''
EX-PY Version: 2.2.0,
A Automation GUI for windows.
Expy released in December, 2023.
It was originally meant to be an external for games,
Now It's an automation GUI for all uses.
Expy was coded in python with tkinter.
''')

pygame.mixer.init()




def load():
    global old
    old = CodeBOX.get("1.0", tk.END)
    path=filedialog.askopenfilename(title="Select a file", filetypes=(("Expy Scripts", "*.expy"),))
    with open(path, 'r') as file:
        content = file.read()
        cprint("Loaded Script:" + file.name)    
    CodeBOX.delete("1.0", tk.END)    
    CodeBOX.insert("insert", content)
def save():
    data = CodeBOX.get("1.0", tk.END)
    path = filedialog.asksaveasfilename(defaultextension=".expy", filetypes=(("Expy Scripts", "*.expy"), ("All files", "*.*")))
    with open(path, 'w') as file:
     file.write(data)
     cprint("Written File: "+file.name)

def RAND_WAIT(v1,v2):
    var = randrange(v1,v2)
    sleep(var)

def WIND_DOUBLE_CLICK(type):
    for i in range(2):
        sleep(0.01)
        mouse.click(type)

def KEY_HOLD(key, time):
    pyautogui.keyDown(key)
    sleep(time)
    pyautogui.keyUp(key)

def KEY_CHOICE(key, key2, time):
    choice = randrange(1,3)
    if choice == 1:
     pyautogui.keyDown(key)
     sleep(time)
     pyautogui.keyUp(key)
    elif choice == 2:
     pyautogui.keyDown(key2)
     sleep(time)
     pyautogui.keyUp(key2)    


def KEY_PRESS(key):
    pyautogui.keyDown(key)
    sleep(0.01)
    pyautogui.keyUp(key)   

def KEY_REPEAT(key, repeated, speed):
    for i in range(repeated):
        pyautogui.keyDown(key)
        sleep(speed)
        pyautogui.keyUp(key)
        sleep(speed)

def WIND_CLICK(type):
    mouse.click(button=type)


def WIND_HOLD_CLICK(type, length):
    mouse.hold(type)
    sleep(length)
    mouse.release(type)

def WIND_MOVE(y,x,abso,dur):
    val = False
    if abso == "yes":
        val = True
    mouse.move(x, y, absolute=val, duration=int(dur))
def M_MOVEDRAG(sx,sy,ex,ey,abso,dur):
    val = False
    if abso == "yes":
        val = True
    mouse.drag(sx,sy,ex,ey,absolute=val,duration=int(dur))

def FUNC_TYPE(message):
     pyautogui.write(message)

def UI_MSG(utype, name, text, hold):
   if utype == "error":
       messagebox.showerror(title=name,message=text)
   elif utype == "warn":
       messagebox.showwarning(title=name,message=text)
   elif utype == "info":
       messagebox.showinfo(title=name,message=text)  
   if hold != None:
       sleep(float(hold))
             
       



def syntax(times, loop,forv):
   global read
   for i in range(times): 
    EXE = CodeBOX.get("1.0", tk.END)
    EXES = EXE.split()
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
                          read = True
                          break
                         elif ans == "no":
                          read = False
                          break
                        if ans == "no":
                            return 
                KEY_HOLD(str(a1), float(a2))
            else:
                next 
        if 'randkey' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1]
                a3 = undersplit[2].split(")")[0]
                KEY_CHOICE(str(a1), str(a2), float(a3))
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
        if 'mousedrag' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1]
                a3 = undersplit[2]
                a4 = undersplit[3]
                a5 = undersplit[4]
                a6 = undersplit[5].split(")")[0]
                M_MOVEDRAG(a1,a2,a3,a4,a5,a6)
            else:
                next  
        if 'tkmessage' in syn and loop == False and forv == False:
            code = syn.split("(")
            if code[1] != None:
                textmess=""
                titlemess=""
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1]
                a3 = undersplit[2]
                a4 = undersplit[3].split(")")[0]

                if '*' in a3:
                    newmess = a3.split("*")
                    for space in newmess:
                        textmess = textmess + " " + space
                else:
                    text=a3        
                if '*' in a2:
                    newmess = a2.split("*")
                    for space in newmess:
                        titlemess = titlemess + " " + space  
                else:
                    titlemess=a2              
                UI_MSG(a1, titlemess, textmess, a4)
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
        if 'randwait' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1].split(")")[0]
                RAND_WAIT(int(a1), int(a2))
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
        if 'playsound' in syn:
            code = syn.split("(")
            if code[1] != None:
                undersplit = code[1].split("_")
                a1 = undersplit[0]
                a2 = undersplit[1].split(")")[0]
                pygame.mixer.music.load(str(a1))
                pygame.mixer.music.set_volume(float(a2))
                pygame.mixer.music.play()
            else:
                next      
        if 'stopallsounds()' in syn:
                pygame.mixer.music.stop()          
        if 'type' in syn:
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
                FUNC_TYPE(message)
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
                syntax(int(undersplit[0]),True,False)
                break
            else:
                next   
        if 'forever()' in syn and loop == False:
            syntax(1,False,True) 


def launch():
     syntax(1,False,False)


def clear():
 global old
 old = CodeBOX.get("1.0", tk.END)
 CodeBOX.delete("1.0", tk.END)
def clearo():
 OutBOX.delete("1.0", tk.END)
def restore():
  CodeBOX.delete("1.0", tk.END)
  CodeBOX.insert("insert",old) 


def on_attach_button():
    att = attach(ProcBOX.get())
    
    if att != None:
     print("Connected To: " + att)
     cprint("Connected To: " + att)
     StatusBOX.config(text="Status: Connected")
    else:
        print("Unable to connect.")
        cprint("Unable to connect.")
        messagebox.showerror("Ex-PY", "Unable to connect.")
        StatusBOX.config(text="Status: Disconnected")

def openraw():
 webbrowser.open('https://raw.githubusercontent.com/twigkid/expy/main/README.md')
def open():
 webbrowser.open('https://github.com/twigkid/expy') 


    

Core = tk.Tk()
Core.geometry("600x370")
Core.title("Ex-PY")


core = Core


Core.resizable(width=False, height=False)
Core.attributes("-topmost", 1)

MainBox = ScrolledText(Core)
MainBox.place(x = 15, y = 9, width=356, height=300)
CodeBOX = MainBox

OutBox = ScrolledText(Core)
OutBox.place(x = 381, y = 9, width=210, height=300)

OutBOX = OutBox

Execute = tk.Button(text="Launch",command=launch)
Execute.place(x=15, y = 320)

Clear = tk.Button(text="Clear",command=clear)
Clear.place(x=100, y = 320)

Restore = tk.Button(text="Restore",command=restore)
Restore.place(x=165, y = 320)

ClearOUT = tk.Button(text="Clear Output",command=clearo)
ClearOUT.place(x=248, y = 320)

Bar = tk.Menu(Core)
menua=tk.Menu(Bar,tearoff=0)
menua.add_command(label="Save", command=save)
menua.add_command(label="Load",command=load)
menua.add_command(label="Exit",command=Core.destroy)
menua.add_command(label="Reboot",command=reboot)
Bar.add_cascade(label="File", menu=menua)

AAA = tk.Menu(Bar,tearoff=0)

AAA.add_command(label="Github",command=open)
AAA.add_command(label="Github (Raw)",command=openraw)
Bar.add_cascade(label="Github", menu=AAA)

About = tk.Menu(Bar, tearoff=0)

About.add_command(label="About Ex-PY",command=about)
Bar.add_cascade(label="About", menu=About)


Core.config(menu=Bar)

Core.mainloop()
