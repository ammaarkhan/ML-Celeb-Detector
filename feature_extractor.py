# mtcnn==0.1.0
# tensorflow--2.3.1
# keras==2.4.3
# keras-vggface==0.6
# keras_applications==1.0.8
# import os
# import pickle
#
# actors = os.listdir('data')
#
# filenames = []
#
# for actor in actors:
#     for imgFile in os.listdir(os.path.join('data', actor)):
#         filenames.append(os.path.join('data', actor, imgFile))
#
# pickle.dump(filenames, open('filenames.pkl', 'wb'))

from tensorflow.keras.preprocessing import image
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
import numpy
import pickle
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

filenames = pickle.load(open('filenames.pkl', 'rb'))

model = VGGFace(model='resnet50', include_top=False, input_shape=(244, 244, 3), pooling='avg')

print(model.summary())