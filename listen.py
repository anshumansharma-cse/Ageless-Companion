# Learning to build the STT phase of Ageless
# ---------------------------------------------------------
# AGELESS Companion : STT Pipeline (Terminal Prints the trascription)
# ---------------------------------------------------------

from faster_whisper import WhisperModel

model_size="large-v3-turbo"
# think about auto imports, like model asked to import numpy
# model=WhisperModel("medium")
model=WhisperModel(model_size, device="auto", compute_type="int8")


segments, info= model.transcribe(
   
    "audio_file" #placeholder
)
print("Detected language:", info.language)
print("\nTranscription:\n")
# NO> segments = list(segments) for streaming (use generator instad, 'cause it's lazy in execution/computation)

# List Version
segments = list(segments)

for segment in segments:
    # print("%[.2fs -> %.2fs] %s" %(segment.start, segment.end, segment.text))
    # The above line follows old school string formatting, C style ("%d", var)
    # use f-strings instead
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")


#  ✅ Generator version (streaming), remove list version
# for segment in segments:
#     print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
# Issues like hallucinations, no fragmentation(chunk size cuts off audio mid-phoneme??), no pause detection, code switching/hindi failure exist ⬆️

