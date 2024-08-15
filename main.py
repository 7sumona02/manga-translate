#translate method 1

import pytesseract
from PIL import Image
import cv2
from googletrans import Translator

image_path = 'images/i5.png'  
image = cv2.imread(image_path)

# Preprocess the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
denoised_image = cv2.fastNlMeansDenoising(gray_image)  # Denoise the image
_, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Thresholding

extracted_text = pytesseract.image_to_string(binary_image, lang='jpn')

translator = Translator()

translated_text = translator.translate(extracted_text, dest='en').text

print(translated_text)