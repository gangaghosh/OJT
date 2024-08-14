# MNIST DATASET

# Import the librarys
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.dataset import mnist
from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D    
from tensorflow.keras.utils import to_categorical
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# load the mnist dataset 
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize the dataset
x_train,x_test=x_train/255.0,x_test/255.0

# reshape the data for CNN
x_train=x_train.reshape(-1,28,28,1)
x_test=x_test.reshape(-1,28,28,1)
# one hot encoding for ann cnn in data
y_train_oh=to_categorical(y_test,10)
y_test_oh=to_categorical(y_test,10)

# build an ANN Model
# the images into 28*28 for the 10 vectors
ann_model=sequential([
     Flatten(input_shape=(28,28,1)),
])

# first hidden layer
Dense(128,activation='relu')

# second hidden layer
Dense(64,activation='relu')

Dense(10,activation='softmax')

# compile the model
ann_model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])

# Train ANN Model
ann_model.fit(x_train,y_train_oh,epochs=5, batch_size=32)
validation_data=(x_test,y_test_oh)

# Evaluate the model
test_loss, test_accuracy = ann_model.eva1uate(x_test, y_test_oh)
print(f'Test loss: {test_loss} ' )
print(f'Test accuracy: {test_accuracy}')





