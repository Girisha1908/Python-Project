# Bhasha - Advanced Multilingual Translator

## 📌 Overview
Bhasha is a **multilingual text and speech translator** built using Python and Tkinter. It allows users to:
- Translate text between multiple languages
- Convert spoken language to text (speech-to-text)
- Read out the translated text (text-to-speech)
- Support multiple languages using Google Translate API

## 🛠 Features
✔️ Translate text between **multiple languages**  
✔️ Speech-to-Text conversion using **Google Speech Recognition**  
✔️ Text-to-Speech functionality using **gTTS (Google Text-to-Speech)**  
✔️ **Multi-threading** for seamless performance  
✔️ Responsive **Tkinter GUI**  
✔️ **Error handling** and user-friendly messages  

## 📌 Technologies Used
- **Python** (Core language)
- **Tkinter** (GUI framework)
- **Googletrans** (Translation API)
- **gTTS** (Text-to-Speech)
- **SpeechRecognition** (Speech-to-Text)
- **Pygame** (Audio playback)
- **Threading** (Background processing)


### ** dependencies **
pip install googletrans==4.0.0-rc1 gtts pygame SpeechRecognition


## 📌 Usage
1. **Enter text** in the input box.
2. **Select languages** for translation.
3. Click **Translate** to get the output.
4. Click **🎤 Record** to input speech.
5. Click **🔊 Speak** to listen to the translation.
6. Click **Clear** to reset the text fields.

## 🎨 User Interface
The interface includes:
- Input Text Area
- Output Text Area
- Language Selection Dropdowns
- Buttons for Translation, Speech Input, Text-to-Speech, and Clearing Fields

## 🛠 Code Structure
- `main.py` → Main script with GUI and core functionality.
  
##💡 Personal Note & Future Work
This is my first ever Python project, and learned a lot while building it. In the future, I plan to add:
 Basic security features to ensure data privacy while translating online:
 
🔐 SSL/TLS Encryption: Ensures all API communication is encrypted and protected.
🛡️ AES Encryption: Securely encrypts text data before sending it for translation.
🚫 No Data Storage Policy: The app does not store user inputs, speech recordings, or translations.



## 🏆 Contributing
Feel free to contribute! Fork the repo, make changes, and submit a pull request.

## 📝 License
This project is open-source and available under the **MIT License**.



