import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values to range [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# Load the trained model
model = tf.keras.models.load_model('number_model.h5')

# Example: Use an image from the test set for prediction
test_image_index = 3456  # Change this index to test different images
test_image = x_test[test_image_index]
test_image = test_image.reshape((1, 28, 28, 1))  # Reshape for model input


# Make predictions
predictions = model.predict(test_image)

# Get the predicted class (number)
predicted_class = np.argmax(predictions)

print(f"Predicted number for the test image at index {test_image_index}: {predicted_class}")

# Verify the actual class
actual_class = y_test[test_image_index]
print(f"Actual number for the test image at index {test_image_index}: {actual_class}")
