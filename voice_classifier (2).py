from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np

speaker_model = {}
encoder = VoiceEncoder()

def add_speaker(speaker_name, audio_file_path):
    fpath = Path(audio_file_path)
    wav = preprocess_wav(fpath)
    encoder = VoiceEncoder()
    embed = encoder.embed_utterance(wav)
    speaker_model[speaker_name] = embed

add_speaker("Milton", "E:/AI/Recording-_5_.wav")

add_speaker("Ernesto", "E:/AI/AUD-20231204-WA0001.wav")

new_audio_path = "E:/AI/AUD-20231204-WA0001.wav"
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