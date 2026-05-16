# AGELESS V1.0

## WHAT will V1 bring on the table?

- Voice First Interface
- Ability to understand and respond to 'native' conversation in native tongue
- Session Info


## How to Create V1
### Must Not a plugin/ wrapper
Creation Plan - Under Review (little Idea)


## Technical Challanges
- How to extract hidden meaning form the speach (words) of person?
- how will Ageless find diffrerences in voice tones, pitch...extract emotion from voice
eg- Voice me kampan, dukh, khushi, uncertainity, motivation, sahas, darr, akela-pan etc kaise identify hoge

## Tech Stack & Current Scope

### V1.0 Stack -->
Basic python(streamlit) dashboard, frome where user may interact with Ageless; it's temporary home
LLM,Conversational Logic -->

V1 Tech Stack — What, Why, How

- Streamlit — the UI
<br>
    What: Browser-based interface, mic input via streamlit-mic-recorder
<br>
    Why: No install, no app store, works on any device, voice-first possible
<br>
    How: User opens browser, speaks, sees/hears response. That's it.

- Sarvam Saarika — ears
<br>
    What: Speech to text
<br>
    Why: Built for Indian accents, Hindi-first, handles Hinglish
<br>
    How: Audio captured → sent to Saarika API → returns text transcript

- Sarvam-1 — brain
<br>
    What: LLM for response generation
<br>
    Why: Understands Hinglish natively, Indian cultural context built in
<br>
    How: Transcript + conversation history + your system prompt → response text

- Sarvam Bulbul — voice
<br>
    What: Text to speech
<br>
    Why: Sounds human, natural Hindi, not robotic
<br>
    How: Response text → Bulbul API → audio plays back automatically

- st.session_state — memory
<br>
    What: In-session conversation history
<br>
    Why: Zero infrastructure, no database, session dies on close
<br>
    How: Every exchange appended to a list, sent with each LLM call

- prompts.py — the soul
<br>
    What: System prompt that defines AGELESS's personality
<br>
    Why: This is where the Indian Subtext Layer lives
<br>
    How: Loaded with every LLM call. Iterated after every real user session.



### Current Scope:
Dont overcomplicate this, no bells & whistles...Simple Ageless, which is able to understand what the user is saying & be able to answer appropriately

### Future Scorpe (AgelessV1.1) -->
Voice Modulations, other
#### How will data collection happen, so that:
1. Ageless will be able to understand 'native' (spoken) conversation
2. Ageless should have an emotional backbone...capable of understanding the 'psyche' of the person using it

