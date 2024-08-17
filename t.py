from googletrans import Translator

text = 'hello'

translator = Translator()

translation = translator.translate(text, src='en', dest='ja').text
print(translation)