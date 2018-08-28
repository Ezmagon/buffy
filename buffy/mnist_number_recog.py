from keras.utils import np_utils
from buffy.resnet164 import ResNet164
from buffy.base_model import BaseModel
import h5py
import numpy as np
from imutils import contours
import imutils
import cv2


def find_numbers(input_image):
    x = input_image
    image = cv2.resize(x, (28, 28))
    # grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = (np.reshape(image, (1, 28, 28, 1)))
    #image = image[np.newaxis, ..., np.newaxis]
    new_axis_image = np.repeat(image[...,None], 1, axis=2)
    new_axis_image = np.repeat(new_axis_image[None, ...], 1, axis=0)
    #image = [image, image]

    divided_image = new_axis_image / 255.0
    f1 = h5py.File('ResNet164.h5')
    model = ResNet164()
    model.load_weights('ResNet164.h5')
    print('Predicting...')
    single_model_prediction = model.predict(divided_image, verbose=1, batch_size=1)
    print(single_model_prediction)
    print(np.argmax(single_model_prediction))
    return np.argmax(single_model_prediction)