"""
Learning to build the STT phase of Ageless
---------------------------------------------------------
AGELESS Companion : STT Pipeline (Terminal Prints the trascription)
---------------------------------------------------------
"""

from faster_whisper import WhisperModel
# File Path Hardcoding (hardcoded environment dependency) issue Solved:->
from pathlib import Path

# Initialse from Project Root:
project_root = Path(__file__).resolve().parent.parent

# Input (Only) File Name (From 'Recordings') :
filename = input("Enter Audio File Name: ")
def get_audio_file(filename): # Later, file path & name both can be parsed
    # PathObj like path
    return (project_root/"Recordings"/filename).resolve()

# Error handling in next iterations

model_size="large-v3-turbo"
# model=WhisperModel("medium")-Initial Testing
# think about auto imports, like model asked to import numpy??
model=WhisperModel(model_size, device="auto", compute_type="int8")

segments, info= model.transcribe(str(get_audio_file(filename)))

print("Detected language:", info.language)
print("\nTranscription:\n")
# NO> segments = list(segments) for streaming (use generator instad, 'cause it's lazy in execution/computation)

# List Version
segments = list(segments)

for segment in segments:
    #
    # print("%[.2fs -> %.2fs] %s" %(segment.start, segment.end, segment.text))
    # The above line follows old school string formatting, C style ("%d", var)
    # use f-strings instead
    #
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")


# Generator Version for Streaming
"""
  ✅ Generator version (streaming), remove list version
 for segment in segments:
     print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
# Issues like hallucinations, no fragmentation(chunk size cuts off audio mid-phoneme??), no pause detection, code switching/hindi failure exist ⬆️
"""