# Speech-Intel
This project captures spoken language, converts it into text, and extracts meaningful insights through Sentiment Analysis and Named Entity Recognition (NER).



## Features
- Converts speech to text using Google's Speech Recognition API.
- Performs Named Entity Recognition (NER) using spaCy.
- Analyzes sentiment using NLTK's SentimentIntensityAnalyzer.
- Saves recorded audio for further processing.

## File Structure
```
|-- speech_ner/
    |-- manage.py
    |-- speech_ner/
        |-- speech/
            |-- templates/
                |-- speech/
                    |-- index.html
            |-- views.py
```

## Installation and Setup

### 1. Clone the Repository
```sh
git clone https://github.com/Mithila-D/Speech-Intel.git
cd Speech-Intel
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install django speechrecognition spacy nltk
python -m spacy download en_core_web_sm
nltk.download('vader_lexicon')
```

### 4. Run the Django Server
```sh
python manage.py runserver
```

### 5. Access the Application
Open your browser and go to:
```
http://127.0.0.1:8000/
```

## Usage
1. Speak into the microphone when prompted.
2. The application will recognize speech, extract named entities, and analyze sentiment.
3. The results will be displayed on the web interface.

## Troubleshooting
- Ensure your microphone is working.
- If `speechrecognition` gives errors, install `pyaudio`:
  ```sh
  pip install pyaudio
  ```
 

