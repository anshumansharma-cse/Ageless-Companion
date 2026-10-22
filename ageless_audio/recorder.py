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



# recording_len=int(input("Enter Recording duration in Seconds: "))
# Audio configuration
FS = 44100          # Sample rate (CD quality)
CHANNELS = 1        # Mono (speech recognition prefers mono)

# Min & Max Recording duration of recordings
Min_Record = 1
Max_Record = 120





# record() is the function which is exposed to FastAPI
# record() accepts recording duration as in I/P from the FrontEnd -> parsed as argument here
def record(duration_seconds: int) -> dict:
    """Records Audio form Local mic & saves WAV file

    Args:
        duration_seconds: Recording duration, as specified by user

    Returns:
        Metadata for the given recording
    """
    if isinstance(duration_seconds, bool) or not isinstance(duration_seconds, int):
        raise TypeError("duration_seconds must be an integer")

    if not Min_Record <= duration_seconds <= Max_Record:
        raise ValueError(f"duration_seconds must be between {Min_Record} and {Max_Record}")

    RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)

    # 10^-9 (Nano-Secnd) level precision (avoids naming conflicts)
    timestamp = time.time_ns()
    #
    filename = RECORDINGS_DIR / f"input_{timestamp}.wav"


    print(f"Recording for {duration_seconds} seconds.\nSpeak now 🗣️...")



    # Record audio
    audio = sd.rec(int(duration_seconds * FS), samplerate=FS, channels=CHANNELS, dtype="int16")
    #dtype="float32" -> float = sounddevice default. use if floating-point audio needed
    # "int16" 16-bit integer sample for WAV files (wider use)

    sd.wait()  # Wait until recording finishes

    # Save recording
    write(filename, FS, audio)

    print(f"Saved as {filename}")

    return {
        "filename": filename.name,
        "path": str(filename),
        "duration_seconds": duration_seconds,
        "sample_rate": FS,
        "channels": CHANNELS
    }




