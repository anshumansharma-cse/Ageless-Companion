from faster_whisper import WhisperModel
from pathlib import Path

# Project Source Folder Declaration
project_root = Path(__file__).resolve().parent.parent
#__file__ is dunder VAR, stores the path to the script

# I/P File Name:
file_name = input("Enter Audio File Name: ")
def get_audio_file(filename):
    return (project_root/"Recordings"/filename).resolve()
# Whisper Model
model_size = "large-v3-turbo"
model = WhisperModel(model_size, device="auto", compute_type="int8")

segments, info = model.transcribe(str(get_audio_file(file_name)))

print("Detected language:", info.language)
print("\nTranscription:\n")

# Generator version (streaming)
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")