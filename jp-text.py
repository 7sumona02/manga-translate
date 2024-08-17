import easyocr
import cv2
from googletrans import Translator
from PIL import Image
import numpy as np

image_path = 'images/i2.jpg' 
image = cv2.imread(image_path)

# Preprocess the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
denoised_image = cv2.fastNlMeansDenoising(gray_image)  # Denoise the image
_, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# initialize easyocr reader 
reader = easyocr.Reader(['ja'])
result = reader.readtext(binary_image)  

# initialize google translator
translator = Translator()

for (bbox, text, prob) in result:
    print(text)  