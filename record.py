
# Learning to build the ears(audio I/P phase) of Ageless
# ---------------------------------------------------------
# AGELESS Companion : Audio Input (Microphone Recorder)
# ---------------------------------------------------------

import time
import sounddevice as sd
from scipy.io.wavfile import write

# Audio configuration
FS = 44100          # Sample rate (CD quality)
SECONDS = 10        # Recording duration
CHANNELS = 1        # Mono (speech recognition prefers mono)

print("Speak now...")

# Record audio
audio = sd.rec(int(SECONDS * FS), samplerate=FS, channels=CHANNELS)
sd.wait()  # Wait until recording finishes

# Create unique filename (prevents overwrite)
filename = f"Recordings/input_{int(time.time())}.wav"

# Save recording
write(filename, FS, audio)

print(f"Saved as {filename}")
