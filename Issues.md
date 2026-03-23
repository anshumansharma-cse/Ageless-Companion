# STT Issues Mapping->
(faster-whisper)
- hallucinations, segmentations, code switching & Indic Language classification issues, Generator module (see test2.wav), merge segments(ignore pause),over-segmentation (saans ke pause par bhi split) ,words lost,phonetic confusion,inaccurate timespamps(not judging pauses as separate segments, sometimes adding/removing it),silence,INCONSISTENCY{List Vs Generator}

## STT Observatiuons (-WhisperModel:"medium")
 | Priority               | Over                    |
 | 1--------------------w | 1---------------------n |
 | 2. sentence completion | 2. precise segmentation |
 | 3.language consistency | 3. exact phonetics      |

semantic flow over silence detection ☝️

- Whisper struggles with minimal phonetic differences in Hinglish ; acoustic alignment bias
- Whisper is NOT sensitive to breath / pause unless strong silence ; segmentation is semantic, not acoustic-first
- Silence + noise → hallucination explosion 👹

---
### -WhisperModel:"large-v3-turbo"
 Now, the STT pipeline is stable, consistent (list & generator based execution-yield similar outputs).
 It has better segmentation, decent accuracy,less hallucinations, greater language preservation.
 Language distortion,Phonetic confusion & Language dominance still remain.
