import tkinter as tk
from tkinter import font
import speech_recognition as sr
from pydub import AudioSegment
import os
from voice_classifier import predict

text_list = []  # Initialize text_list as an empty list

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f'{index}, {name}')

def start_recognition():
    global recognizer
    try:
        with sr.Microphone(device_index=3) as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio_data = recognizer.listen(mic)
            
            # Convert AudioData to AudioSegment
            audio = AudioSegment(
                audio_data.frame_data,
                sample_width=audio_data.sample_width,
                frame_rate=audio_data.sample_rate,
                channels=1  # assuming mono audio
            )

            text = recognizer.recognize_google(audio_data, language="id-ID")
            text = text.lower()
            print(text)
            

            # Save the audio to 'cur.wav' in the same directory as the script
            script_directory = os.path.dirname(os.path.abspath(__file__))
            audio_path = os.path.join(script_directory, 'cur.wav')
            print(audio_path)
            save_audio(audio, audio_path)

            identified_speaker = predict()  # Get the identified speaker from the predict function
            print(identified_speaker)
            # Update the Listbox with the recognized text and color based on the identified speaker
            if identified_speaker == 'Bryan':
                text_listbox.insert(tk.END, text)
                text_listbox.itemconfig(tk.END, {'fg': 'yellow'})
            elif identified_speaker == 'Milton':
                text_listbox.insert(tk.END, text)
                text_listbox.itemconfig(tk.END, {'fg': 'blue'})
            else:
                text_listbox.insert(tk.END, text)

            recognized_text.set(f"Recognized: {text}")

            text_list.append(text)

    except sr.UnknownValueError:
        pass

def save_audio(audio, filename):
    # Export the AudioSegment to a WAV file
    audio.export(filename, format="wav")

def stop_recognition():
    global recognizer
    recognizer = sr.Recognizer()

app = tk.Tk()
app.title("Speech Recognition GUI")
app.configure(bg='#5d8a82')  # Set background color to black
app.geometry('600x400')  # Set window size to 400 x 300

# Use Roboto font and increase the font size
font_style = font.Font(family='Roboto', size=12)

recognized_text = tk.StringVar()

# Frame for buttons on the left
button_frame = tk.Frame(app, bg='#5d8a82')
button_frame.pack(side=tk.LEFT, padx=20)

# Make button background blue with white text
start_button = tk.Button(button_frame, text="Start Recognition", command=start_recognition, bg='#007BFF', fg='black', bd=2, highlightbackground='#5d8a82', font=font_style, borderwidth=3, relief="groove")
stop_button = tk.Button(button_frame, text="Stop Recognition", command=stop_recognition, bg='#007BFF', fg='black', bd=2, highlightbackground='#5d8a82', font=font_style, borderwidth=3, relief="groove")

start_button.pack(pady=10)
stop_button.pack(pady=10)

# Textbox on the right
text_listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=40, width=40, bg='black', fg='white', font=font_style)
text_listbox.pack(side=tk.RIGHT, padx=20, pady=10)

# Output label on the right
# output_label = tk.Label(app, textvariable=recognized_text, bg='#5d8a82', fg='white', font=font_style)
# output_label.pack(side=tk.RIGHT, padx=20)

recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000

app.mainloop()
