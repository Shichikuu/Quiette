from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
import os
def open_file_in_same_directory(file_name):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   file_path = os.path.join(script_dir, file_name)

   return file_path

speaker_model = {}
encoder = VoiceEncoder()

def add_speaker(speaker_name, file_name):
    fpath = Path(open_file_in_same_directory(file_name))
    wav = preprocess_wav(fpath)
    encoder = VoiceEncoder()
    embed = encoder.embed_utterance(wav)
    speaker_model[speaker_name] = embed

add_speaker("Milton", "Recording-_5_.wav")
add_speaker("Bryan", "cookies.wav")
add_speaker("Ernesto", "AUD-20231204-WA0001.wav")

# Feature yang bisa ditambahin: Voice Classifier untuk unknown/orang tidak dikenal

def predict():
    new_audio_path = open_file_in_same_directory("cur.wav")
    new_wav = preprocess_wav(Path(new_audio_path))
    new_embed = encoder.embed_utterance(new_wav)

    # Compare the new embedding with the stored embeddings
    min_distance = float('inf')
    identified_speaker = None

    for speaker_name, speaker_embed in speaker_model.items():
        distance = np.linalg.norm(new_embed - speaker_embed)
        if distance < min_distance:
            min_distance = distance
            identified_speaker = speaker_name

    print(f"Identified Speaker: {identified_speaker}")
    return identified_speaker

predict()