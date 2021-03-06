from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Activation, Dropout, Flatten, Dense

# dimensions of our images.
img_width, img_height = 150, 150

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 400
nb_validation_samples = 400
nb_epoch = 15

#Create the model
model = Sequential()

#Layer 1
#model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(64, 3, 3, input_shape = (3, img_width, img_height)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides = (2, 2)))

#Layer 2
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(128, 3, 3))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(128, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides = (2, 2)))

#Layer 3
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(256, 3, 3))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(256, 3, 3))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(256, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides = (2, 2)))

#Layer 4
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(512, 3, 3))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(512, 3, 3))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(512, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides = (2, 2)))

#Layer 5
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(512, 3, 3))
model.add(Activation('relu'))
(ZeroPadding2D((1, 1)))
model.add(Convolution2D(512, 3, 3))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1, 1)))
model.add(Convolution2D(512, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides = (2, 2)))

#Layer 6
model.add(Flatten())

model.add(Dense(256, init = 'uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(1, init = 'uniform'))
model.add(Activation('sigmoid'))
###########################
###CREATE THE CONV MODEL###
###########################


model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode='binary')

model.fit_generator(
        train_generator,
        samples_per_epoch=nb_train_samples,
        nb_epoch=nb_epoch,
        validation_data=validation_generator,
        nb_val_samples=nb_validation_samples)

#model.load_weights('first_try.h5')
