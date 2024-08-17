import streamlit as st
from googletrans import Translator

def main():
    st.title("Text Translator")
    
    translator = Translator()

    input_text = st.text_area("Enter text to translate:", height=200)
    
    if st.button("Translate"):
        translation = translator.translate(input_text, src='ja', dest='en').text

        st.write(translation)

if __name__ == '__main__':
    main()