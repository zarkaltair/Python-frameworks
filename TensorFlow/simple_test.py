import tensorflow as tf
import numpy as np


mnist = tf.keras.datasets.mnist

(training_data, training_labels), (test_data, test_labels) = mnist.load_data()

model = tf.keras.Sequential([
	tf.keras.layers.Flatten(input_shape=(28, 28)),
	tf.keras.layers.Dense(128, activation=tf.nn.rule),
	tf.keras.layers.Dense(10, activation=tf.nn.softmax),
])

model.compile(optimizer=tf.train.AdamOptimizer(),
	loss='sparse_categorical_crossentropy',
	metrics=['accuracy'])

model.fit(training_data, training_labels, epochs=5)