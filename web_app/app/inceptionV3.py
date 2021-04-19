from flask import Flask

import numpy as np
import os, shutil
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

model = load_model('app/inception')

def generate_output(prediction, acc, op):
   op["neutral"] = "none"
   op["acc"] = "Prediction ~ " + str(int(acc * 100)) + "% Chances"
   if prediction == 0:
      op["color"] = "green"
      op["nonidc"] = "block"
   else:
      op["color"] = "red"
      op["idc"] = "block"  
   shutil.rmtree("/mnt/c/Users/USER/Documents/BE Project/breast-cancer/main/app/static/uploads")
   os.mkdir("/mnt/c/Users/USER/Documents/BE Project/breast-cancer/main/app/static/uploads")

def classify(image, op):
   global model
   image = load_img('app/static/uploads/' + image, target_size = (150, 150))
   image = img_to_array(image)
   image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
   image = preprocess_input(image)
   pred = model.predict(image)
   if pred[0][0] > pred[0][1]:
      print("0 --> Non IDC")
      generate_output(0, pred[0][0], op)
   else:
      print("1 --> IDC")
      generate_output(1, pred[0][1], op)
