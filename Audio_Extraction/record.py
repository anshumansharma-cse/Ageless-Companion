
# Learning to build the ears(audio I/P phase) of Ageless
# ---------------------------------------------------------
# AGELESS Companion : Audio Input (Microphone Recorder)
# ---------------------------------------------------------

import time
import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path

# Future Scope- Ability to handle vaeious I/P formats like 10 minutes, 1hr 5 min, etc.
# Using 'datetime' module

# Recorder is Independent of cwd
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RECORDINGS_DIR = PROJECT_ROOT / "Recordings"

Recording_len=int(input("Enter Recording duration in Seconds: "))
# Audio configuration
FS = 44100          # Sample rate (CD quality)
SECONDS = Recording_len        # Recording duration
CHANNELS = 1        # Mono (speech recognition prefers mono)

print("Speak now...")

# Record audio
audio = sd.rec(int(SECONDS * FS), samplerate=FS, channels=CHANNELS)
sd.wait()  # Wait until recording finishes

# Create unique filename (prevents overwrite)
filename = RECORDINGS_DIR/f"input_{int(time.time())}.wav"

# Save recording
write(filename, FS, audio)

print(f"Saved as {filename}")
