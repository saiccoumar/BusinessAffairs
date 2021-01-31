from json.encoder import JSONEncoder
import os
import webview
import threading
import time
import sys
import random
import json

from pathlib import Path
from webview.guilib import initialize

running = True

class Api():
    # def detecting(self):
    #     #time.sleep(1)
    #     global running
    #     import os
    #     import datetime
    #     DATA_DIR = os.path.join(os.getcwd(), 'data')
    #     MODELS_DIR = os.path.join(DATA_DIR, 'models')
    #     for dir in [DATA_DIR, MODELS_DIR]:
    #         if not os.path.exists(dir):
    #             os.mkdir(dir)

    #     #print("raasd")
    #     start = datetime.datetime.now()
    #     import tarfile
    #     import urllib.request

    #     # Download and extract model
    #     MODEL_DATE = '20200711'
    #     MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'

    #     #'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
    #     #'ssd_resnet101_v1_fpn_640x640_coco17_tpu-8' 
    #     MODEL_TAR_FILENAME = MODEL_NAME + '.tar.gz'
    #     MODELS_DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/tf2/'
    #     MODEL_DOWNLOAD_LINK = MODELS_DOWNLOAD_BASE + MODEL_DATE + '/' + MODEL_TAR_FILENAME
    #     PATH_TO_MODEL_TAR = os.path.join(MODELS_DIR, MODEL_TAR_FILENAME)
    #     PATH_TO_CKPT = os.path.join(MODELS_DIR, os.path.join(MODEL_NAME, 'checkpoint/'))
    #     PATH_TO_CFG = os.path.join(MODELS_DIR, os.path.join(MODEL_NAME, 'pipeline.config'))
    #     if not os.path.exists(PATH_TO_CKPT):
    #         print('Downloading model. This may take a while... ', end='')
    #         urllib.request.urlretrieve(MODEL_DOWNLOAD_LINK, PATH_TO_MODEL_TAR)
    #         tar_file = tarfile.open(PATH_TO_MODEL_TAR)
    #         tar_file.extractall(MODELS_DIR)
    #         tar_file.close()
    #         os.remove(PATH_TO_MODEL_TAR)
    #         print('Done')
    #     print("downloading model:" + str(datetime.datetime.now() - start))
    #     start = datetime.datetime.now()

    #     # Download labels file
    #     LABEL_FILENAME = 'mscoco_label_map.pbtxt'
    #     LABELS_DOWNLOAD_BASE = \
    #         'https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/data/'
    #     PATH_TO_LABELS = os.path.join(MODELS_DIR, os.path.join(MODEL_NAME, LABEL_FILENAME))
    #     if not os.path.exists(PATH_TO_LABELS):
    #         print('Downloading label file... ', end='')
    #         urllib.request.urlretrieve(LABELS_DOWNLOAD_BASE + LABEL_FILENAME, PATH_TO_LABELS)
    #         print('Done')
    #     print("downloading labels:" + str(datetime.datetime.now() - start))
    #     start = datetime.datetime.now()
    #     os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging
    #     import tensorflow as tf
    #     from object_detection.utils import label_map_util
    #     from object_detection.utils import config_util
    #     from object_detection.utils import visualization_utils as viz_utils
    #     from object_detection.builders import model_builder

    #     tf.get_logger().setLevel('ERROR')           # Suppress TensorFlow logging (2)

    #     # Enable GPU dynamic memory allocation
    #     gpus = tf.config.experimental.list_physical_devices('GPU')
    #     for gpu in gpus:
    #         tf.config.experimental.set_memory_growth(gpu, True)

    #     # Load pipeline config and build a detection model
    #     configs = config_util.get_configs_from_pipeline_file(PATH_TO_CFG)
    #     model_config = configs['model']
    #     print(model_config)
    #     detection_model = model_builder.build(model_config=model_config, is_training=False)
    #     print("building model:" + str(datetime.datetime.now() - start))
    #     start = datetime.datetime.now()
    #     # Restore checkpoint
    #     ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
    #     ckpt.restore(os.path.join(PATH_TO_CKPT, 'ckpt-0')).expect_partial()
    #     print("restore cp:" + str(datetime.datetime.now() - start))
    #     start = datetime.datetime.now()
    #     @tf.function
    #     def detect_fn(image):
    #         """Detect objects in image."""

    #         image, shapes = detection_model.preprocess(image)
    #         prediction_dict = detection_model.predict(image, shapes)
    #         detections = detection_model.postprocess(prediction_dict, shapes)

    #         return detections, prediction_dict, tf.reshape(shapes, [-1])

    #     category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
    #                                                                         use_display_name=True)

    #     import cv2

    #     cap = cv2.VideoCapture(0)
    #     import numpy as np
    #     import subprocess, sys
    #     from pynput.keyboard import Key, Listener
    #     #set up keybinds
    #     keybinds = {"pause": "p", "minimize": "m", "mute": "s", "blackout": "b"}
    #     currentPressed = set()
    #     def on_press(key):
    #         print(key)
    #         currentPressed.add(key)
    #         try:
    #             key = key.char
    #             currentPressed.add(key)
    #         except AttributeError :
    #             currentPressed.add(key)

    #         if(key == keybinds["minimize"]):
    #             path = os.getcwd()
    #             p = subprocess.Popen(["powershell.exe", 
    #                 path + "\\minimize.ps1"], 
    #                 stdout=sys.stdout)
    #             p.communicate()
    #         if(key == keybinds["blackout"]):
    #             path = os.getcwd()
    #             p = subprocess.Popen(["powershell.exe", 
    #                 path + "\\monitor.ps1"], 
    #                 stdout=sys.stdout)
    #             p.communicate()
    #         if(key == keybinds["pause"]):
    #             running = not running
    #         if(Key.shift in currentPressed and Key.ctrl_l in currentPressed):
    #             print("combo")

    #     def on_release(key):
    #         currentPressed.remove(key)
    #         print('{0} release'.format(
    #             key))
    #         if key == Key.esc:
    #             # Stop listener
    #             return False

    #     # Collect events until released
    #     listener = Listener(
    #             on_press=on_press,
    #             on_release=on_release)
    #     listener.start()

    #     print("rest of setup model:" + str(datetime.datetime.now() - start))
    #     start = datetime.datetime.now()
    #     while True:

    #         # Read frame from camera
    #         ret, image_np = cap.read()

    #         # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    #         image_np_expanded = np.expand_dims(image_np, axis=0)

    #         # Things to try:
    #         # Flip horizontally
    #         # image_np = np.fliplr(image_np).copy()

    #         # Convert image to grayscale
    #         # image_np = np.tile(
    #         #     np.mean(image_np, 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

    #         input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)

    #         detections, predictions_dict, shapes = detect_fn(input_tensor)
    #         print("detection:" + str(datetime.datetime.now() - start))
    #         start = datetime.datetime.now()
    #         label_id_offset = 1
    #         image_np_with_detections = image_np.copy()
    #         #print(detections.keys())
    #         """viz_utils.visualize_boxes_and_labels_on_image_array(
    #               image_np_with_detections,
    #               detections['detection_boxes'][0].numpyp(),
    #               (detections['detection_classes'][0].numpy() + label_id_offset).astype(int),
    #               detections['detection_scores'][0].numpy(),
    #               category_index,
    #               use_normalized_coordinates=True,
    #               max_boxes_to_draw=200,
    #               min_score_thresh=.50,
    #               agnostic_mode=False)"""

    #         # Display output
    #         #print("showing")
    #         #cv2.imshow('object detection', cv2.resize(image_np_with_detections, (800, 600)))
    #         flag = False
    #         stop = False
    #         numPeople = 0
    #         if(running):
    #             for i in range(len((detections['detection_classes'][0].numpy() + label_id_offset).astype(int)   )):
    #                 item = (detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i]
    #                 if(detections['detection_scores'][0].numpy()[i] < .60):
    #                     continue;
    #                 #print(category_index[item]["name"])
    #                 if(category_index[item]["name"] == "person"):
    #                     flag = True
    #                     numPeople += 1
    #             #print(numPeople)
    #             if(numPeople >= 1):
    #                 print("too many people!" + str(len(detections['detection_classes'][0])))
    #                 continue
    #         #print(category_index[(detections['detection_classes'][0].numpy() + label_id_offset).astype(int)    [0]]    ['name'])
    #         if cv2.waitKey(25) & 0xFF == ord('q'):
    #             break

    #     cap.release()
    #     cv2.destroyAllWindows()
    #     listener.stop()    

    # Detecting process
    def detecting(self):
        while running:
            print("DETECTING GOING ON")
            time.sleep(5)

    # Updates global running variable for detector
    def updateRunning(self, value):
        global running
        if not value:
            running = False
        else:
            running = True
        print(running)


    # Configuration window
    def createConfigWindow(self):
        configWindow.show()     

    # Config save and exit
    def configSaveExit(self):
        configWindow.hide()


    # Status functions
    def onClosed(self):
        print('Running closing actions.')
        configWindow.destroy()
        print('Closing actions completed. Safely terminated.')
    def onLoaded(self):
        print('Application is fully loaded.')
        configWindow.hide()

    # Settings
    def readSettings(self):
        global prefAudio, prefVideo, prefMin, prefDesktop, prefMute, prefBlack, prefPeople, prefToggle, prefOpen, prefTerminate, prefTrigger
        with open('pref.json') as json_file:
            pref = json.load(json_file)
            for p in pref['av']:
                prefAudio = p['audio']
                prefVideo = p['video']
            for p in pref['behavior']:
                prefMin = p['min']
                prefDesktop = p['desktop']
                prefMute = p['mute']
                prefBlack = p['black']
                prefPeople = p['people']
            for p in pref['keybinds']:
                prefToggle = p['toggle']
                prefOpen = p['open']
                prefTerminate = p['terminate']
                prefTrigger = p['trigger']
        print('Preferences were read.')
        return [[prefAudio,prefVideo],[prefMin,prefDesktop,prefMin,prefBlack,prefPeople],[prefToggle,prefOpen,prefTerminate,prefTrigger]]
    def writeSettings(self, videoDev, audioDev, behaviors, people, keybinds):
        tempSet = {}
        tempSet['av'] = []
        tempSet['av'].append({
            'audio': audioDev,
            'video': videoDev
        })
        tempSet['behavior'] = []
        tempSet['behavior'].append({
            'min': behaviors[0],
            'desktop': behaviors[1],
            'mute': behaviors[2],
            'black': behaviors[3],
            'people': people
        })
        tempSet['keybinds'] = []
        tempSet['keybinds'].append({
            'toggle': keybinds[0],
            'open': keybinds[1],
            'terminate': keybinds[2],
            'trigger': keybinds[3]
        })
        print(tempSet)
        with open('pref.json','w') as outfile:
            json.dump(tempSet,outfile)
        print('Preferences were written.')
        api.readSettings()

if __name__ == '__main__':
    api = Api()

    # Check if settings exist and then write
    settings = Path('pref.json')
    if settings.is_file():
        print('Settings exists. Reading settings.')
        api.readSettings()
    else:
        print('No settings found. The following settings will be configured:')
        api.writeSettings(0,0,[True, False, False, False],1,['Ctrl + Shift + B', 'Ctrl + Shift + B', 'Ctrl + Shift + X', 'Ctrl + Shift + E'])

    # Define windows
    mainWindow = webview.create_window('BusinessAffairs', 'assets/index.html', js_api=api, width=1000, height=750, resizable=False, text_select=False)
    configWindow = webview.create_window('Configuration', 'assets/config.html', js_api=api, width=900, height=900, resizable=False, frameless=True, on_top=True, text_select=False)

    # Detecting actions
    mainWindow.closed += api.onClosed
    mainWindow.loaded += api.onLoaded

    # Start UI
    webview.start()