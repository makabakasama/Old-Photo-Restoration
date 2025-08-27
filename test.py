import numpy as np
import cv2
import PySimpleGUI as sg
import os.path
import argparse
import os
import sys
import shutil
from subprocess import call

images_col = [[sg.Text('Input file:'), sg.In(enable_events=True, key='-IN FILE-'), sg.FileBrowse()],
              [sg.Button('Modify Photo', key='-MPHOTO-'), sg.Button('Exit')],
              [sg.Image(filename='', key='-IN-'), sg.Image(filename='', key='-OUT-')], ]
# ----- Full layout -----
layout = [[sg.VSeperator(), sg.Column(images_col)]]

# ----- Make the window -----
window = sg.Window('Bringing-old-photos-back-to-life', layout, grab_anywhere=True)

# ----- Run the Event Loop -----
prev_filename = colorized = cap = None
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    elif event == '-MPHOTO-':
        try:
            print(filename)

        except:
            continue

    elif event == '-IN FILE-':  # A single filename was chosen
        filename = values['-IN FILE-']
        if filename != prev_filename:
            prev_filename = filename
            try:
                image = cv2.imread(filename)
                window['-IN-'].update(data=cv2.imencode('.png', image)[1].tobytes())
            except:
                continue

# ----- Exit program -----
window.close()