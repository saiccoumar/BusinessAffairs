import json
import os
import webbrowser
from functools import wraps
from flask import Flask, render_template, jsonify, request
import webview
import app
import subprocess, sys
from pynput.keyboard import Key, Listener



# mac code
bashHide = "osascript src/backend/scripts/scriptMinimize.scpt"
bashShow= "osascript src/backend/scripts/scriptUndo.scpt"
bashMute= "osascript src/backend/scripts/scriptMute.scpt"
bashUnmute = "osascript src/backend/scripts/scriptUnmute.scpt"
bashSleep = "osascript src/backend/scripts/scriptSleep.scpt"
bashDesktop = "osascript src/backend/scripts/scriptNewDesktop.scpt"

gui_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'gui')  # development path

# if not os.path.exists(gui_dir):  # frozen executable path
#     gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui')

path = os.path.dirname(__file__)
dir = path[0:len(path)-11]

server = Flask(__name__, static_folder=dir + '/static', template_folder=dir+'/gui')
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching
# can write more functions for different functionality.

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
    if((Key.shift in currentPressed) and (Key.ctrl_l in currentPressed)):
        global volume
        if (volume):
            mute()
        elif (volume==False):
            unmute()
        print("combo")
def on_release(key):
    currentPressed.remove(key)
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

def minimizeWindows():
    proc = os.popen(bashHide)
    output = proc.read()
def show():
    proc = os.popen(bashShow)
    output = proc.read()
volume = True
def mute():
    proc = os.popen(bashMute)
    output = proc.read()
    global volume
    volume = False
def unmute():
    proc = os.popen(bashUnmute)
    output = proc.read()
    global volume
    volume = True
def sleep():
    proc = os.popen(bashSleep)
    output = proc.read()
def newDesktop():
    proc = os.popen(bashDesktop)
    output = proc.read()

listener = Listener(
        on_press=on_press,
        on_release=on_release)


@server.route('/')
def landing():
    # manualHide()
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('setup.html')

@server.route('/monitor', methods=["POST"])
def monitor():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    var = request.form['monitoringButton']
    
    if var == "Not Monitoring":
        return render_template('index.html', monitoringTF = "Monitoring")
        # listener.start()
        # list1 = list(range(100000))
        # while running:
        #     list1.append(list1.pop(0))
        # # listener.stop()
    else:
        return render_template('index.html', monitoringTF = "Not Monitoring")
        # listener.stop()
        
    
        


@server.route('/test')
def test():
    bruh = "yesyesyes"
    # mute()
    bruh = gui_dir
    # webview.create_window('My second pywebview application', server)
    return render_template('index.html',monitoringTF = "Not Monitoring")

@server.route('/config')
def scanVideo():
    bruh = "config"
    # calls minimize windows based on video input
    # likely needs a conditional to check for toggle to watch is on, if off video should be disabled
    return render_template('config.html',value = bruh)
    print("config")

@server.route('/camera')
def scanAudio():
    # calls minimize windows based on audio input
    # likely needs a conditional to check for toggle to listen is on, if off audio should be disabled
    bruh = "camera"
    return render_template('config.html')
    print("camera")

# @server.route('/manual')
# def manualHide():
    # calls minimize windows based on a keybind
    
    # print("manual")






