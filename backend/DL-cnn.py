import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import pickle
import joblib
#import pillow



TrainingImagePath = 'Face Images/Final Training Images'
TestingImagePath = 'Face Images/Final Testing Images'
#Preprocessing Training Set

train_datagen = ImageDataGenerator(
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
)

training_set = train_datagen.flow_from_directory(
    TrainingImagePath,
    target_size = (64,64),
    batch_size = 32,
    class_mode = 'categorical'
)
#Preprocessing Test Set
test_datagen = ImageDataGenerator(
    rescale = 1./255
)

test_set = test_datagen.flow_from_directory(
    TestingImagePath,
    target_size = (64,64),
    batch_size = 32,
    class_mode = 'categorical'
)
#test_set.class_indices

TrainClasses = training_set.class_indices
ResultMap = {}
for faceValue, faceName in zip(TrainClasses.values(), TrainClasses.keys()):
    ResultMap[faceValue] = faceName

#import pickle
#with open("ResultMap.pkl", "wb") as fileWriteStream:
 #   pickle.dump(ResultMap, fileWriteStream)

OutputNeurons = len(ResultMap)
#print('Mapping of face and its IDs :', ResultMap)
#print('\n The Number of Output Neurons:',len(ResultMap) )

#CNN
"""
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import Maxpool2D
from keras.layers import Flatten
from keras.layers import Dense
"""

cnn = tf.keras.models.Sequential()

cnn.add(tf.keras.layers.Conv2D(filters = 32, kernel_size = (2, 2), strides = (1, 1),padding = 'valid',  activation = 'relu', input_shape = [64, 64, 3]))

cnn.add(tf.keras.layers.MaxPool2D(pool_size = (2, 2)))

cnn.add(tf.keras.layers.Conv2D(64, kernel_size=(3, 3), strides=(1, 1), activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size = (2, 2)))

cnn.add(tf.keras.layers.Flatten())

cnn.add(tf.keras.layers.Dense(64, activation = 'relu'))

cnn.add(tf.keras.layers.Dense(OutputNeurons, activation = 'softmax'))

#Compile

cnn.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

#Train

import scipy
import time
#StartTime = time.time()

cnn.fit(x = training_set, validation_data = test_set, epochs = 25 )

#EndTime = time.time()

#Pickle export

cnn.save('model.keras')

#pickle.dump(cnn, open("model.pkl", "wb"))

#print('Total time taken:', round(EndTime - StartTime),'seconds')


""""
from keras.preprocessing import image
import  numpy as np
test_image = image.load_img('Face Images/Final Testing Images/face8/4face8.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image, verbose=0)
#print('####'*10)
#print('Prediction is: ',ResultMap[np.argmax(result)])

#******************use pickle to access model in app.py**********************************

"""























