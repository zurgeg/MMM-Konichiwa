# This runs the server for the module to connect to

print('Usage: Run, then press Ctrl+V and then type "bg"')

import socket
import mahotas
import cv2
import os
import h5py

class State:
    def __init__(self):
        self._camera = camera = cv2.VideoCapture(0)
    def take_pic(self):
        return self._camera.read()
print('[KONICHIWA] Finished loading modules...')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 1234))

# From https://gogul.dev/software/image-classification-python

def fd_hu_moments(image):
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      feature = cv2.HuMoments(cv2.moments(image)).flatten()
      return feature
def fd_haralick(image):
      # convert the image to grayscale
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      # compute the haralick texture feature vector
      haralick = mahotas.features.haralick(gray).mean(axis=0)
      # return the result
      return haralick
def fd_histogram(image, mask=None):
    # convert the image to HSV color-space
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # compute the color histogram
    hist  = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    # normalize the histogram
    cv2.normalize(hist, hist)
    # return the histogram
    return hist.flatten()
def on_identify_command(client):
    image = state.take_pic()
    image = cv2.resize(image, (640, 480))

    ####################################
    # Global Feature extraction
    ####################################
    fv_hu_moments = fd_hu_moments(image)
    fv_haralick   = fd_haralick(image)
    fv_histogram  = fd_histogram(image)
state = State() # Stores stuff like the camera
print('[KONICHIWA] State created...')



