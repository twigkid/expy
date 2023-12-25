![plot](./icons/expy.png)  # Ex-PY

Ex-PY: External Python

Supports: Windows;

An automation GUI for all applications.

# Installation (WINDOWS 7 - 8 - 10 - 11)

Expy works on the latest version of python and windows

Expy uses Tkinter for it's UI, It won't run without it.
1st, Open a new terminal and paste in:

```pip install tk```

2nd, Install PyAutoGUI
Run the code in a terminal below:
```pip install pyautogui```


Once finished, you will need to download the latest version of Expy
You can find the .py file in the releases tab.

# Running ExPy

To run ExPy you need to have the packages above installed, If you do then follow these steps below:
Right click the file
Find "Open With"
Select and click Python (MAKE SURE IT HAS NO NUMBERS)

A terminal window will pop up and about half a second later Expy will load.

# Attaching

To Attach to an application simply hover over the app you're trying to use and look at it's name and write it into the textbox besides "Execute"
After that's done click "Attach" and your window will be put on top, showing that It was successful

# Expy's Language

The first version of Expy only has two functions which are:
```chat() # RBLX Only``` and ```holdkey()```
To use chat simply do ```chat(yourmessagehere)```
Expy's language doesn't use "" or , Instead It uses and underscore _



# DOCUMENTATION FOR EXPY CLAM

# CONNECTING / ATTACHING:
Type the program's .exe name into the small textbox besides connect,
After that click "Connect" and wait until the application responds with "Connected."
Then you can run your code by pressing "Launch"


# FUNCTIONS:

Functions: ```chat(word_otherword), holdkey(letter_number), repeatkey(letter_times_speed), leave(), reset(), jump(), pause(time), click(left or right), mousehold(left or right, time), mousemove(x, y), loop(times)```

# CHAT:
Chat is used with roblox.
Type ```chat()``` into the large textbox,
you can type any word into the textbox that has no spaces.
To add spaces the the message add an underscore like this: ```chat(hello_world!)```

# HOLDKEY:
Type ```holdkey()``` into the large textbox,
the first argument must be a single letter, lowercase or uppercase.
the second argument must be a number.
EXAMPLE: ```holdkey(w_1)```

# REPEAT KEY:
Type ```repeatkey()``` into the large textbox,
the first argument must be a single letter, lowercase or uppercase.
the second argument must be a number, this number is the ammount of times the key is repeated.
the third argument also must be a number, this number is the speed of the repeat.

# LEAVE:
It will leave the game if EXPY is connected to roblox.

# RESET:
It will reset the player's character if EXPY is connected to roblox

# JUMP:
It will jump in any game if connect to the program

# PAUSE:
Pauses and yeilds execution until the time with-in the brackets is met.

# CLICK:
  This can be rather left or right. It will click on the application
  
# MOUSEHOLD:
  Works like ```click()``` but with an extra argument which holds the mouse until the time is met

# MOUSEMOVE:
  This has two arguments, X & Y. The mouse will move to the coordinates.
# LOOP:
  Loops the program for the ammount of times inside the brackets.
  


For the holdkey function do this:
```holdkey(yourkey_number)```
The number is the ammount of time the key is held, 0 will just be a key click.
yourkey must only be one character, like this: "w_1" "s_1" "d_1" "a_1"

# Execution

To run your code inside the textbox simply click "Execute" and It will automatically run your code.
