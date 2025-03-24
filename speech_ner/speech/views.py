
############################################
import speech_recognition as sr
import spacy
import os
from django.shortcuts import render
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
 
nlp = spacy.load("en_core_web_sm")
 
nltk.download('vader_lexicon')
 
sia = SentimentIntensityAnalyzer()

def speech_to_text(request):
    text = ""
    entities = []
    sentiment = {}

    if request.method == "POST":
        recognizer = sr.Recognizer()
        audio_filename = "speech/audio.wav"
 
        os.makedirs("speech", exist_ok=True)

        with sr.Microphone() as source:
            print(" Speak now... Recording...")
            recognizer.adjust_for_ambient_noise(source)
            #   audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            audio = recognizer.listen(source)
 
        with open(audio_filename, "wb") as f:
            f.write(audio.get_wav_data())

        print(f" Audio recorded and saved as {audio_filename}")
 
        try:
            with sr.AudioFile(audio_filename) as source:
                print(" Processing recorded audio...")
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)

            print("\n Recognized Text:", text)
 
            doc = nlp(text)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
 
            sentiment = sia.polarity_scores(text)

        except sr.UnknownValueError:
            text = " Could not understand the audio."
        except sr.RequestError:
            text = " Error with the speech recognition service."

    return render(request, "speech/index.html", {"text": text, "entities": entities, "sentiment": sentiment})
