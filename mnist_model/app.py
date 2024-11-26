import tensorflow as tf
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np


def preprocess_image(image_path, new_size=(28, 28)):
    with Image.open(image_path) as img:
        
        grayscale_image = ImageOps.grayscale(img)
        
        resized_image = grayscale_image.resize(new_size)
        
        #inverted_image = ImageOps.invert(resized_image)
        
        normalized_image = np.array(resized_image) / 255.0
        
        preprocessed_image = normalized_image.reshape((1, 28, 28, 1))

        plt.imshow(normalized_image, cmap='gray')
        plt.title("Preprocessed Image")
        #plt.show()

    return preprocessed_image

# Load the MNIST model (replace this with your own model loading code)
model = tf.keras.models.load_model('number_model.h5')

# Path to the input image
input_image_path = "openCVpic.jpg"

# Preprocess the input image
preprocessed_image = preprocess_image(input_image_path)

# Make predictions
predictions = model.predict(preprocessed_image)

# Get the predicted class (number)
predicted_class = np.argmax(predictions)

print("Predicted number:", predicted_class)
