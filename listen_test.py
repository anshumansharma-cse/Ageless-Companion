from faster_whisper import WhisperModel

model_size = "large-v3-turbo"
model = WhisperModel(model_size, device="auto", compute_type="int8")

segments, info = model.transcribe(
    "audio_file" #placeholder

)

print("Detected language:", info.language)
print("\nTranscription:\n")

# Generator version (streaming)
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")