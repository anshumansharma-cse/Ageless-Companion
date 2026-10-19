""" Module for Ageless-Companion Backend audio recording functionality """

# ----------------------------------------------------------------------
# AGELESS Companion : Audio Input (Microphone Recorder) - Dynamic Module
# ----------------------------------------------------------------------

import time
import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path


# Recorder is Independent of cwd
PROJECT_ROOT = Path(__file__).resolve().parent
RECORDINGS_DIR = PROJECT_ROOT / "audio_file"

# record() is the function which is exposed to FastAPI
def record():
    recording_len=int(input("Enter Recording duration in Seconds: "))
    # Audio configuration
    FS = 44100          # Sample rate (CD quality)
    SECONDS = recording_len        # Recording duration
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


# record()

