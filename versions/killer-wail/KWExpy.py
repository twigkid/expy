import pyautogui
from tkinter import *
import tkinter as tk
import keyboard
from time import sleep

rbxwin = 0
window = 0
attached = False

application = ""

# Functions



def chat(message):
  if window != 0:
     window.activate()
     keyboard.send("/")
     sleep(0.3)
     keyboard.write(message)
     sleep(0.2)
     keyboard.press("enter")
     sleep(0.3)
     keyboard.release("enter")
def presskey(key):
 if attached == True:
   window.activate()  
   keyboard.press(key)
def holdkey(key, time):
 if attached == True:  
  window.activate()
  if not time:
    presskey(key)
  else:
   keyboard.press(key)
   sleep(time)
   keyboard.release(key)    



# Creating the GUI
   
main = tk.Tk()
main.title("expy")
main.geometry("400x200")

main.resizable(width=False, height=False)
main.attributes("-topmost", 1)

box = tk.Entry(main)
box.pack()
box.place(x=15, y=0)

lab = tk.Label(main, text="Status: Unattached")
lab.place(x = 0, y = 180)

winname = tk.Entry(main)
winname.place(x=180,y=173,width=100)

# UI Functions
   
def attach_int(processname):
 windows = pyautogui.getWindowsWithTitle(processname) # Finds the Roblox Window.
 if windows and windows[0].title == processname: # Checks if the window exists
    ex_win = windows[0]
    ex_win.activate()
    global rbxwin
    global window
    global attached
    if ex_win:
      rbxwin = 1
      lab.config(text = "Status: Attached")
      window = ex_win
      attached=True
    else:
      rbxwin = 0
      window=0
      attached=False
      lab.config(text = "Status: unattached")
 if not windows:
   rbxwin = 0
   lab.config(text = "App not found!")
   sleep(0.75)
   lab.config(text = "Status: unattached")

inbut=0

def send_msg():
  chat(box.get())  

def attach():
   p = winname.get()
   attach_int(p)

button = tk.Button(main, text = "Send Message (RBLX ONLY)", command=send_msg)
button.place(x=150,y=0, height = 20)

inject = tk.Button(main, text = "Attach", command=attach)
inject.place(x=350,y=170)

inbut=inject

if rbxwin == 1:
   lab.config(text = "Status: Attached")
elif rbxwin == 0:
  lab.config(text = "Status: Unattached")

## MAIN CODE BOX
    


tb = tk.Entry(main)
tb.pack(anchor="nw", expand=True, fill="both")
tb.place(x = 15, y = 30, width=350, height = 130)

BLoop = False

def execute():
  global BLoop
  if attached == True:
    m = tb.get()
    split = m.split()
    if BLoop == False:
     for word in split:
      if word.find("chat("):
       splittedb = word.split("holdkey(")
       if splittedb[1]:
        final = splittedb[1].split(")")
        if final[0].find("_"):
          key=0
          time=0
          space = final[0].split("_")
          key = space[0]
          time = space[1]
          print(key, time)
          holdkey(key, float(time))
     if word.find("holdkey("):
      splittedc = word.split("chat(")
      print(splittedc)
      if splittedc[1]:
        final = splittedc[1].split(")")
        if final[0].find("_"):
          mess = ""
          space = final[0].split("_")
          for wo in space:
            mess = mess + " " + wo
          chat(mess)
    else:
      while BLoop == True:
        sleep(0.01)
        m = tb.get()
        split = m.split()
        print(split)
        for word in split:
         if word.find("chat("):
          splittedb = word.split("holdkey(")
          if splittedb[1]:
           final = splittedb[1].split(")")
           if final[0].find("_"):
             key=0
             time=0
             space = final[0].split("_")
             key = space[0]
             time = space[1]
             holdkey(key, float(time))
           if word.find("holdkey("):
            splittedc = word.split("chat(")
            print(splittedc)
            if splittedc[1]:
              final = splittedc[1].split(")")
              if final[0].find("_"):
                mess = ""
                space = final[0].split("_")
                for wo in space:
                   mess = mess + " " + wo
                chat(mess)
        if keyboard.is_pressed('ctrl+z'):
          break        

a=0

def loop():
  global BLoop
  BLoop = not BLoop
  if BLoop == True:
    a.config(text="Loop: Yes")
  else:
    a.config(text="Loop: No")  

              
exe = tk.Button(main, text = "Execute", command=execute)
exe.place(x=290,y=170)

looop = tk.Button(main, text = "Loop: No", command=loop)
looop.place(x=115,y=170)

a=looop

main.mainloop()

