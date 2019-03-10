import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

images_x = []
images_y = []
directories = ["earth", "jupiter", "mars", "mercury", "saturn", "uranus"]
model = keras.Sequential({
	keras.layers.Convolution2D(32, 3, 3, batch_input_shape = (128, 128, 3), activation='relu'),
	keras.layers.MaxPooling2D(pool_size = (2, 2)),
	keras.layers.Flatten(),
	keras.layers.Dense(128, activation='relu'),
	keras.layers.Dropout(0.5),
	keras.layers.Dense(128, activation='relu'),
	keras.layers.Dense(6, activation='softmax')
})

def doStuff():
	load()
	generate()

def load():
	global images_x
	global images_y
	for num, folder in enumerate(directories):
		for file in os.listdir("train/" + folder):
			if file != ".DS_Store":
				image = img_to_array(load_img("train/" + folder + "/" + file, target_size=(128, 128)))
				
				print(image.shape)
				#image = Image.open("train/" + folder + "/" + file).convert('L').resize((128, 128), Image.ANTIALIAS)
				#image = np.asarray(image.getdata(),dtype=np.float64).reshape((image.size[1],image.size[0])) / 255.
				images_x.append(image)
				images_y.append(num)

def generate():
	'''global images_x
	global images_y
	images_x1 = np.array(images_x).reshape(94, 128, 128, 1)
	images_y1 = np.array(images_y)
	images_x = images_x1
	images_y = images_y1'''
	global images_x
	global images_y
	print(np.array(images_x).shape)
	model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
	model.fit(np.array(images_x), np.array(images_y), epochs = 20, verbose = 1)


def test():
	model.predict_classes(images_x[0].reshape(1, 128, 128))


if __name__ == '__main__':
	doStuff()