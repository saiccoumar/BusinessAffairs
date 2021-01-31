import json
import os
import webbrowser
from functools import wraps
from flask import Flask, render_template, jsonify, request,redirect
import webview
import app
import subprocess, sys
from pynput.keyboard import Key, Listener
# from multiprocessing import Process, Value
import threading



camera = ""
audio = ""
min = ""
desktop= ""
mute= ""
black= ""
monitor= ""
open= ""
end= ""
value = ""
path = os.path.dirname(__file__)
dir = path[0:len(path)-11]
print(dir)

# mac code
bashHide = "osascript src/backend/scripts/scriptMinimize.scpt"
bashShow= "osascript src/backend/scripts/scriptUndo.scpt"
bashMute= "osascript src/backend/scripts/scriptMute.scpt"
bashUnmute = "osascript src/backend/scripts/scriptUnmute.scpt"
bashSleep = "osascript src/backend/scripts/scriptSleep.scpt"
bashDesktop = "osascript src/backend/scripts/scriptNewDesktop.scpt"
bashExit = "kill -9 888"

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

def startKeybind():
    listener = Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    list1 = list(range(100000))
    while running:
        list1.append(list1.pop(0))
    # if (monitor == "Not Monitoring"):
    #     listener.stop()
x = threading.Thread(target=startKeybind)

@server.route('/')
def landing():
    
    MODELS_DIR = dir + "/models"
    # manualHide()
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('setup.html',value = dir)

@server.route('/monitor', methods=["POST"])
def monitor():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    var = request.form['monitoringButton']
    

    if var == "Not Monitoring":
        # x.start()
        print("hjk")
        x.start()
        # return render_template('index.html', monitoringTF = "Monitoring")
    elif var == "Monitoring":
        
        # proc = os.popen(bashExit)
        # output = proc.read()
        x.join()
        # return render_template('index.html', monitoringTF = "Not Monitoring")
        # listener.stop()
    if var == "Monitoring":
        # x.start()
        # x.join()
        return render_template('index.html', monitoringTF = "Not Monitoring")
    else:
        # x.start()
        return render_template('index.html', monitoringTF = "Monitoring")
        # listener.stop()
    
        
    
        
@server.route('/setup',methods = ["POST"])
def setup():
    global camera
    global audio
    global value 
    if request.method == "POST":
        camera = request.form['videoInput']
        audio = request.form['audioInput']
        value = "setup"
    return redirect('/test', code=302)

@server.route('/back',methods = ["POST"])
def back():
    global camera
    global audio
    global min
    global desktop
    global mute
    global black
    global monitor
    global open
    global end
    global value
    # value = "config"
    if request.method == "POST":
        camera = request.form['videoInput']
        audio = request.form['audioInput']
        min = request.form['min']
        desktop= request.form['desktop']
        mute= request.form['mute']
        black= request.form['black']
        monitor= request.form['monitor']
        open= request.form['open']
        end= request.form['end']
        value = "config"
    return redirect('/test', code=302)

@server.route('/test', methods=["GET","POST"])
def test():
    
    bruh = "yesyesyes"
    # mute()
    bruh = gui_dir
    # webview.create_window('My second pywebview application', server)
    return render_template('index.html',monitoringTF = "Not Monitoring",camera = value )

@server.route('/config')
def config():
    bruh = "config"
    # calls minimize windows based on video input
    # likely needs a conditional to check for toggle to watch is on, if off video should be disabled
    return render_template('config.html',camera = camera, audio = audio, min = min, desktop = desktop, mute = mute, black= black, monitor=monitor, open = open, end=end, value = value)
    print("config")


# @server.route('/manual')
# def manualHide():
    # calls minimize windows based on a keybind
    
    # print("manual")






