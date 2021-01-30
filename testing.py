"""import os
import subprocess, sys
path = os.getcwd()
print(path + "\\minimize.ps1")
p = subprocess.Popen(["powershell.exe", 
              path + "\\minimize.ps1"], 
              stdout=sys.stdout)
p.communicate()"""
import subprocess, sys
"""from pynput import keyboard
keybinds = {"pause": "p", "minimize": "m", "mute": "s", "blackout": "b"}
running = True
def action(key):
    if(keybinds["pause"] == key.char):
        print("ih")
    if(keybinds["minimize"] == key.char):
        print("hi")
#keybinds = {"pause": "p", "minimize": "m", "mute": "s", "blackout": "b"}
listener = keyboard.Listener(
    on_press=action,
    on_release=None)
listener.start()"""

from pynput.keyboard import Key, Listener
import os, subprocess
currentPressed = set() 
running = True
def on_press(key):
    try:
        currentPressed.add(key)
        print('alphanumeric key {0} pressed'.format(
            key))
    except AttributeError:
        currentPressed.add(key)
        print('special key {0} pressed'.format(
            key))
    if(Key.shift in currentPressed and Key.ctrl_l in currentPressed):
        global running
        running = False
        print("combo")
    """if(key.char == "p"):
        path = os.getcwd()
        p = subprocess.Popen(["powershell.exe", 
            path + "\\minimize.ps1"], 
            stdout=sys.stdout)
        p.communicate()"""

def on_release(key):
    currentPressed.remove(key)
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released

listener = Listener(
        on_press=on_press,
        on_release=on_release)
listener.start()
list1 = list(range(100000))
while running:
    list1.append(list1.pop(0))
listener.stop()