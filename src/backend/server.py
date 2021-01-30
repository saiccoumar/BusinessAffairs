import json
import os
import webbrowser
from functools import wraps
from flask import Flask, render_template, jsonify, request
import webview
import app





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

server = Flask(__name__, static_folder=dir + '/statics', template_folder=dir+'/gui')
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching
# can write more functions for different functionality.
def minimizeWindows():
    proc = os.popen(bashHide)
    output = proc.read()
def show():
    proc = os.popen(bashShow)
    output = proc.read()
def mute():
    proc = os.popen(bashMute)
    output = proc.read()
def sleep():
    proc = os.popen(bashSleep)
    output = proc.read()
def newDesktop():
    proc = os.popen(bashDesktop)
    output = proc.read()


@server.route('/')
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('index.html')

@server.route('/test')
def test():
    bruh = "yesyesyes"
    # mute()
    bruh = gui_dir
    # webview.create_window('My second pywebview application', server)
    return render_template('setup.html',value = bruh)

@server.route('/video')
def scanVideo():
    # calls minimize windows based on video input
    # likely needs a conditional to check for toggle to watch is on, if off video should be disabled
    print("video")

@server.route('/audio')
def scanAudio():
    # calls minimize windows based on audio input
    # likely needs a conditional to check for toggle to listen is on, if off audio should be disabled
    print("audio")

@server.route('/manual')
def manualHide():
    # calls minimize windows based on a keybind
    print("manual")






