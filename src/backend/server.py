import json
import os
import webbrowser
from functools import wraps

from flask import Flask, render_template, jsonify, request
import webview
import app

gui_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'gui')  # development path

if not os.path.exists(gui_dir):  # frozen executable path
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui')

server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching




@server.route('/')
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('index.html')


