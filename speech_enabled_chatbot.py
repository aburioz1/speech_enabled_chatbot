import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st
import speech_recognition as sr

# Load the text file and preprocess the data
#nltk.download('punkt')
with open('nature.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')
data = data.lower()
sentences = nltk.sent_tokenize(data)
words = nltk.word_tokenize(data)

# Define a function to transcribe speech into text
def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."
    except sr.RequestError:
        return "Sorry, unable to access the speech recognition service."


# Modify the chatbot function to take both text and speech input from the user
def chatbot(input):
    response = ""

    for sentence in sentences:
        if sentence.lower().startswith(input.lower()):
            response = sentence.lower().replace(input.lower(), "").strip()
            break

    if not response:
        response = "Sorry, I don't understand."

    return response

# Create a Streamlit app that allows the user to provide either text or speech input to the chatbot
st.title("Speech-Enabled Chatbot")

# Text input
text_input = st.text_input("Type your question or command here:")

# Speech input
speech_input = transcribe_speech()

if text_input:
    response = chatbot(text_input)
elif speech_input:
    response = chatbot(speech_input)
else:
    response = ""

st.write(response)
