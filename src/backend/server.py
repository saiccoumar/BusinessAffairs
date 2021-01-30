import json
import os
import webbrowser
from functools import wraps

from flask import Flask, render_template, jsonify, request
import webview
import app

gui_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'gui')  # development path

#if not os.path.exists(gui_dir):  # frozen executable path
#    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui')

path = os.path.dirname(__file__)
dir = path[0:len(path)-11]

server = Flask(__name__, static_folder=dir + '/static', template_folder=dir+'/gui')
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching

#server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
#server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching




@server.route('/')
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('index.html')

@server.route('/test')
def render():
    bruh = "yesyesyesyes"
    # webview.create_window('My second pywebview application', server)
    return render_template('index.html',value = bruh)



