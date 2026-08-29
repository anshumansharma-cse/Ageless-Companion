"""
Ageless STT Module-1
---------------------------------------------------------
AGELESS Companion : STT Testing Pipeline (Terminal Prints the transcription)
---------------------------------------------------------
Faster-Whisper Testing
"""

from faster_whisper import WhisperModel
# File Path Hardcoding (hardcoded environment dependency) issue Solved:->
from pathlib import Path

# Initialise from Project Root:
project_root = Path(__file__).resolve().parent.parent

# Input (Only) File Name (From 'Recordings') :
filename = input("Enter Audio File Name: ")
def get_audio_file(filename): # Later, file path & name both can be parsed
    # Resolve the input filename against the project's Recordings dir
    return (project_root / "Recordings" / filename).resolve()

# Error handling in next iterations

model_size = "large-v3-turbo"
# model=WhisperModel("medium")-Initial Testing
# think about auto imports, like model asked to import numpy??
model = WhisperModel(model_size, device="auto", compute_type="int8")

segments, info = model.transcribe(str(get_audio_file(filename)))

print("Detected language:", info.language)
print("\nTranscription:\n")

# ✅ Generator version (lazy evaluation; straeaming like)
for segment in segments:
     print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

# Known areas for later evaluation:
# hallucinations, segmentation/timestamp quality, pause detection,
# fragmentation, code-switching, Hindi/Indic-language performance, etc.

# -----

# List Version (Remove Generator Version)
"""
segments = list(segments)
# NO> segments = list(segments) for streaming (use generator insted, because it's lazy in execution/computation)
# Meaning:
# Converting the generator to a list forces all segments to be
# generated before the loop processes them.
# The generator version is preferred for lazy evaluation.

for segment in segments:
    #
    # print("%[.2fs -> %.2fs] %s" %(segment.start, segment.end, segment.text))
    # The above line follows old school string formatting, C style ("%d", var)
    # use f-strings instead
    #
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
"""