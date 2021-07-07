from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


# Preprocessing the Training set
train_data = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
training_set = train_data.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')
# Preprocessing the Testing set
test_data = ImageDataGenerator(rescale = 1./255)
test_set = test_data.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')
# Creating model
model = Sequential()

# Adding 1st convo layer
model.add(Conv2D(filters=32, 
                kernel_size=3,
                activation='relu',
                input_shape=[64, 64, 3]))

# Adding 1st Pooling layer
model.add(MaxPooling2D(pool_size=2,
                       strides=2))

# Adding 2nd convo layer
model.add(Conv2D(filters=64, 
                kernel_size=3,
                activation='relu',
                ))

# Adding 2nd Pooling layer
model.add(MaxPooling2D(pool_size=2,
                       strides=2))

# Adding Flattening layer
model.add(Flatten())

# creating Dence layer
model.add(Dense(units=128,
                activation='relu'))

# Adding outout layer
model.add(Dense(units=1,
                activation='sigmoid'))

# Compiling model
model.compile(optimizer="adam",
              loss='binary_crossentropy',
              metrics='accuracy')

# Training Data
model.fit(x=training_set, validation_data=test_set, epochs=100)

# Saving Model
model.save("BT_MODEL-v1.h5")


print("Model Successfully created..")
