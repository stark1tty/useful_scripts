import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers.experimental import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight

print("Setting up parameters...")
# Set the path to your dataset directory
data_dir = "X:/Dropbox/Pollen_AI_Project/pollen-ai/Rotated_Images"

# Set the desired batch size, image dimensions, and number of classes
batch_size = 512
img_height = 255
img_width = 255
num_classes = 264  # Update this to match the actual number of classes in your data

print("Collecting image paths and labels...")
# Get a list of all file paths and corresponding labels
all_image_paths = []
all_image_labels = []
class_names = os.listdir(data_dir)
for label, class_name in enumerate(class_names):
    class_dir = os.path.join(data_dir, class_name)
    image_paths = [os.path.join(class_dir, img) for img in os.listdir(class_dir)]
    image_labels = [label] * len(image_paths)
    all_image_paths.extend(image_paths)
    all_image_labels.extend(image_labels)

print("Splitting data into training and validation sets...")
# Split the data into training and validation sets
train_paths, val_paths, train_labels, val_labels = train_test_split(
    all_image_paths, all_image_labels, test_size=0.2, stratify=all_image_labels, random_state=123)

print("Calculating class weights...")
# Calculate class weights
class_weights = class_weight.compute_sample_weight('balanced', train_labels)
class_weights = dict(enumerate(class_weights))

print("Creating training dataset...")
# Create a dataset from the training set
train_ds = tf.data.Dataset.from_tensor_slices((train_paths, train_labels))
train_ds = train_ds.map(lambda x, y: (tf.image.resize(tf.image.decode_jpeg(tf.io.read_file(x), channels=1), [img_height, img_width]), y))
train_ds = train_ds.batch(batch_size)

print("Creating validation dataset...")
# Create a dataset from the validation set
val_ds = tf.data.Dataset.from_tensor_slices((val_paths, val_labels))
val_ds = val_ds.map(lambda x, y: (tf.image.resize(tf.image.decode_jpeg(tf.io.read_file(x), channels=1), [img_height, img_width]), y))
val_ds = val_ds.batch(batch_size)

print("Defining the model architecture...")
# Define the model architecture
model = keras.Sequential([
    keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(img_height, img_width, 1)),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(num_classes)  # remove the softmax activation here
])

print("Compiling the model...")
# Compile the model
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"]
)

print("Training the model...")
# Train the model
history = model.fit(
    train_ds,
    epochs=10,
    validation_data=val_ds,
    class_weight=class_weights  # Use class weights
)

print("Printing model summary...")
# Print model summary
model.summary()

print("Saving the model...")
model.save('pollen_1_512')

print("Done!")
