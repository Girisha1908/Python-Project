'''from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import threading
import pygame
import os
import speech_recognition as sr

# Initialize the main window
root = Tk()
root.geometry('1100x400')
root.resizable(0, 0)
root.title("Bhasha - Advanced Multilingual Translator")
root['bg'] = '#2C3E50'

# Style configuration for combobox
style = ttk.Style()
style.theme_use('clam')
style.configure('TCombobox', fieldbackground='#34495E', background='#34495E', foreground='white')

# Main header
Label(root, text="Multilingual Translator", font="arial 24 bold", bg='#3498DB', fg='white', pady=10).pack(fill=X)

# Input and Output Labels and Text Areas
Label(root, text="Enter Text", font='arial 13 bold', bg='#2C3E50', fg='#ECF0F1').place(x=165, y=70)
Input_text = Text(root, font='arial 12', height=5, width=50, wrap=WORD, bg='#34495E', fg='white')
Input_text.place(x=30, y=100)

Label(root, text="Output", font='arial 13 bold', bg='#2C3E50', fg='#ECF0F1').place(x=780, y=70)
Output_text = Text(root, font='arial 12', height=5, width=50, wrap=WORD, bg='#34495E', fg='white', pady=5, padx=5)
Output_text.place(x=600, y=100)

# Language selection dropdowns
language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values=['Auto'] + language, width=22)
src_lang.place(x=30, y=230)
src_lang.set('Auto')  # Default to Auto-detect

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=300, y=230)
dest_lang.set('english')  # Default to English

# Function to translate text
def Translate():
    try:
        src_language = src_lang.get()
        dest_language = dest_lang.get()

        if not dest_language or dest_language == '':
            messagebox.showerror("Translation Error", "Please select a destination language.")
            return

        translator = Translator()
        translated = translator.translate(text=Input_text.get(1.0, END).strip(),
                                          src=None if src_language.lower() == 'auto' else src_language,
                                          dest=[k for k in LANGUAGES.keys() if LANGUAGES[k].lower() == dest_language.lower()][0])
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Function to record audio and convert to text
def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            Input_text.delete(1.0, END)
            Input_text.insert(END, text)
        except sr.UnknownValueError:
            messagebox.showwarning("Speech Recognition", "Could not understand audio")
        except sr.RequestError as e:
            messagebox.showerror("Speech Recognition Error", str(e))

# Function to convert translated text to speech
def speak_text():
    text = Output_text.get(1.0, END).strip()
    if text:
        try:
            lang_name = dest_lang.get()

            if not lang_name or lang_name == '':
                messagebox.showerror("Text-to-Speech Error", "Please select a destination language.")
                return

            lang_code_dict = {v.lower(): k for k, v in LANGUAGES.items()}
            lang_code = lang_code_dict.get(lang_name.lower())

            if not lang_code:
                messagebox.showwarning("Text-to-Speech", f"Language not supported for TTS: {lang_name}")
                return

            # Save audio file safely
            save_path = os.path.join(os.path.expanduser("~"), "Desktop", "output.mp3")
            
            # Ensure pygame is stopped before overwriting the file
            pygame.mixer.init()
            if pygame.mixer.get_init():
                pygame.mixer.quit()
            
            tts = gTTS(text=text, lang=lang_code)
            tts.save(save_path)

            pygame.mixer.init()
            pygame.mixer.music.load(save_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                root.update()

            pygame.mixer.quit()  # Properly close pygame
            os.remove(save_path)  # Delete file after playing

        except Exception as e:
            messagebox.showerror("Text-to-Speech Error", str(e))

# Function to clear input and output fields
def clear_text():
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)

# Buttons for Translate, Record Audio, Speak Text and Clear Text
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5,
                   command=lambda: threading.Thread(target=Translate).start(),
                   bg='#E74C3C', fg='white', activebackground='#C0392B')
trans_btn.place(x=200, y=280)

record_btn = Button(root, text='🎤 Record', font='arial 12 bold', pady=5,
                    command=lambda: threading.Thread(target=record_audio).start(),
                    bg='#2ECC71', fg='white', activebackground='#27AE60')
record_btn.place(x=320, y=280)

speak_btn = Button(root, text='🔊 Speak', font='arial 12 bold', pady=5,
                   command=lambda: threading.Thread(target=speak_text).start(),
                   bg='#3498DB', fg='white', activebackground='#2980B9')
speak_btn.place(x=440, y=280)

clear_btn = Button(root, text='Clear', font='arial 12 bold', pady=5,
                   command=clear_text,
                   bg='#95A5A6', fg='white', activebackground='#7F8C8D')
clear_btn.place(x=560, y=280)

root.mainloop()'''

from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import threading
import pygame
import os
import speech_recognition as sr
import math

# Initialize the main window
root = Tk()
root.geometry('1200x550')
root.resizable(0, 0)
root.title("Bhasha - Advanced Multilingual Translator")
root['bg'] = '#1A1A2E'

# Style configuration for combobox
style = ttk.Style()
style.theme_use('clam')
style.configure('TCombobox', fieldbackground='#16213E', background='#0F3460', foreground='white')

# Global variables for waveform animation
recording_animation_running = False
waveform_phase = 0

# Main header
Label(root, text="🎙️ Multilingual Translator", font="arial 26 bold", bg='#0F3460', fg='white', pady=10).pack(fill=X)

# Input and Output Labels and Text Areas
Label(root, text="Enter Text", font='arial 13 bold', bg='#1A1A2E', fg='white').place(x=180, y=80)
Input_text = Text(root, font='arial 12', height=6, width=50, wrap=WORD, bg='#16213E', fg='white')
Input_text.place(x=30, y=110)

Label(root, text="Output", font='arial 13 bold', bg='#1A1A2E', fg='white').place(x=880, y=80)
Output_text = Text(root, font='arial 12', height=6, width=50, wrap=WORD, bg='#16213E', fg='white')
Output_text.place(x=700, y=110)

# Language selection dropdowns
language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values=['Auto'] + language, width=22)
src_lang.place(x=30, y=260)
src_lang.set('Auto')

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=300, y=260)
dest_lang.set('english')

# Function to translate text
def Translate():
    try:
        src_language = src_lang.get()
        dest_language = dest_lang.get()
        if not dest_language:
            messagebox.showerror("Translation Error", "Please select a destination language.")
            return

        translator = Translator()
        lang_code_dict = {v.lower(): k for k, v in LANGUAGES.items()}

        src_code = lang_code_dict.get(src_language.lower()) if src_language.lower() != 'auto' else None
        dest_code = lang_code_dict.get(dest_language.lower())

        if not dest_code:
            messagebox.showerror("Translation Error", f"Invalid destination language: {dest_language}")
            return

        text_to_translate = Input_text.get(1.0, END).strip()
        if not text_to_translate:
            messagebox.showwarning("Empty Input", "Please enter text to translate.")
            return

        if src_code:
            translated = translator.translate(text=text_to_translate, src=src_code, dest=dest_code)
        else:
            translated = translator.translate(text=text_to_translate, dest=dest_code)  # Auto-detect source

        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


# Waveform animation
def start_waveform_animation():
    global recording_animation_running, waveform_phase
    recording_animation_running = True
    while recording_animation_running:
        canvas.delete("all")
        for i in range(10):
            x = 20 + i * 20
            height = 10 + 10 * math.sin(waveform_phase + i * 0.5)
            canvas.create_line(x, 40, x, 40 - height, fill="#00FFFF", width=3)
        waveform_phase += 0.3
        canvas.update()
        root.after(50)
    canvas.delete("all")

# Audio recording and recognition
def record_audio():
    global recording_animation_running
    recording_animation_running = True
    threading.Thread(target=start_waveform_animation).start()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            Input_text.delete(1.0, END)
            Input_text.insert(END, text)
        except sr.UnknownValueError:
            messagebox.showwarning("Speech Recognition", "Could not understand audio")
        except sr.RequestError as e:
            messagebox.showerror("Speech Recognition Error", str(e))
        except sr.WaitTimeoutError:
            messagebox.showinfo("Timeout", "No voice input detected.")
        finally:
            recording_animation_running = False
            canvas.delete("all")

# Text-to-speech
def speak_text():
    text = Output_text.get(1.0, END).strip()
    if text:
        try:
            lang_name = dest_lang.get()
            lang_code_dict = {v.lower(): k for k, v in LANGUAGES.items()}
            lang_code = lang_code_dict.get(lang_name.lower())
            if not lang_code:
                messagebox.showwarning("Text-to-Speech", f"Language not supported for TTS: {lang_name}")
                return

            save_path = os.path.join(os.path.expanduser("~"), "Desktop", "output.mp3")
            pygame.mixer.init()
            if pygame.mixer.get_init():
                pygame.mixer.quit()

            tts = gTTS(text=text, lang=lang_code)
            tts.save(save_path)

            pygame.mixer.init()
            pygame.mixer.music.load(save_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                root.update()

            pygame.mixer.quit()
            os.remove(save_path)

        except Exception as e:
            messagebox.showerror("Text-to-Speech Error", str(e))

# Clear text fields
def clear_text():
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)

# Centered Buttons
button_frame = Frame(root, bg='#1A1A2E')
button_frame.place(relx=0.5, y=320, anchor=CENTER)

Button(button_frame, text='Translate', font='arial 12 bold', pady=5,
       command=lambda: threading.Thread(target=Translate).start(),
       bg='#E94560', fg='white', activebackground='#B83B5E').grid(row=0, column=0, padx=10)

Button(button_frame, text='🎤 Record', font='arial 12 bold', pady=5,
       command=lambda: threading.Thread(target=record_audio).start(),
       bg='#0F3460', fg='white', activebackground='#1A1A2E').grid(row=0, column=1, padx=10)

Button(button_frame, text='🔊 Speak', font='arial 12 bold', pady=5,
       command=lambda: threading.Thread(target=speak_text).start(),
       bg='#00ADB5', fg='white', activebackground='#007A7A').grid(row=0, column=2, padx=10)

Button(button_frame, text='Clear', font='arial 12 bold', pady=5,
       command=clear_text, bg='#393E46', fg='white', activebackground='#222831').grid(row=0, column=3, padx=10)

# Waveform canvas centered between text boxes
canvas = Canvas(root, width=250, height=60, bg='#1A1A2E', highlightthickness=0)
canvas.place(relx=0.5, y=390, anchor=CENTER)

root.mainloop()
