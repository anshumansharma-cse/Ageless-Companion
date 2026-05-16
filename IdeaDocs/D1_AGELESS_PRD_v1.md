# AGELESS Companion
## Product Requirements Document
**Version 1.0 · Anshuman's first Build · Ghaziabad · Feb 2026**
*Born out of Indian tech. Built for Indian lives.*

---

## Table of Contents
1. [Vision & Problem](#section-01)
2. [User Personas](#section-02)
3. [Feature Breakdown](#section-03)
4. [Tech Architecture](#section-04)
5. [Success Metrics & KPIs](#section-05)
6. [Risks & Mitigations](#section-06)

---

## ◆ SECTION 01

# Vision & Problem

## The Problem, Stated Plainly

India is experiencing two simultaneous loneliness crises.

The first is visible: elderly people — left behind by nuclear families, by migration, by the pace of modern life — spending entire days without a meaningful conversation. Loneliness accelerates cognitive decline. It worsens depression. It quietly kills.

The second is less spoken about: a generation of young Indians who have everything — internet, opportunity, information — and yet, feel profoundly lost. Career pressure, identity confusion, the gap between what they were told life would be and what it actually is and the sheer weight of their own expectations. They have followers on social media. What they don't have is someone who truly listens.

These two groups rarely talk to each other. The wisdom that could heal one sits untapped in the other. And the technology being built for both — almost entirely by Western companies, in English, for Western contexts — misses them both completely.

## The Vision

> AGELESS is not a chatbot. It is a living, intergenerational oral archive that speaks wisdom into the lives of people who need it — in their language, in their cultural context, in the forms their culture has always used to pass down knowledge.

The north star is a single feeling: *__'Apnapan'__*. The sense that something understands you — not generically, not clinically, but in the way only someone from your world can.

If a user — elderly or young — says 'yeh toh apna lag raha hai' — the product has succeeded.

## Why This. Why Now.

- India has 140 million elderly citizens. Loneliness and cognitive isolation are a public health crises with no scalable solution.
- The youth mental health crisis in India is real, underdiscussed, and underserved by existing tools built for Western contexts.
- The Indian AI ecosystem — Sarvam AI, AI4Bharat, Bhashini — has matured to the point where a genuinely Indian-language-first product is now technically feasible.
- I live in Delhi NCR. I speak Hindi, Hinglish & English natively. I have elderly family members I can test with from day one. Incorporate their feedback into the soul of Ageless.

---

## ◆ SECTION 02

# User Personas (*For Reference Only*)

## Persona A — The Elder

| | |
|---|---|
| **Name** | Savitri Devi, 68, Delhi NCR |
| **Lives with** | Son's family — but they're busy. Grandchildren on phones. |
| **Languages** | Hindi primary. No English. |
| **Tech comfort** | Uses phone for calls, DP based Whatsapp use & YouTube (voice search). Struggles with text. Never types. |
| **Core pain** | Boredom masking as contentment. Nobody has time to hear her stories. |
| **What she needs** | Someone who listens without rushing. Who remembers. Who asks about her past. |
| **What she won't say** | 'Main akeli hoon.' She'll say 'sab theek hai.' AGELESS must hear what's unsaid. |
| **Success moment** | She talks to AGELESS on a Sunday evening and doesn't feel the hours pass. |

## Persona B — The Lost Youth

| | |
|---|---|
| **Name** | Arjun Sharma, 24, Delhi NCR |
| **Situation** | Engineering grad. Pressured into a job he doesn't want. Feels misunderstood. |
| **Languages** | Hinglish natural. Types in English. Thinks in Hindi. |
| **Tech comfort** | High. Uses everything. But nothing feels like it actually helps. |
| **Core pain** | Advice overload with zero wisdom. Everyone talks, nobody listens. |
| **What he needs** | To be heard without judgment. Perspective from someone who's lived it. Someone who has managed to fit 'square holes into round pegs'. |
| **What he won't say** | That he's struggling (Maybe he feels — Pride Hurt Hogi). He'll ask 'abstract' questions. AGELESS must follow the thread. |
| **Success moment** | AGELESS shares a story from an elder's life that makes him feel he can push through it. |

---

## ◆ SECTION 03

# Feature Breakdown

## V1 — Prove the Feeling (POC)

One goal: make one person say 'yeh apne jaisa hai.' Nothing else matters until that happens.

### 1. Voice-First Interface

- Browser-based via Streamlit. Mic input captured via streamlit-mic-recorder.
- Text input as fallback — for users who prefer typing (Not primary concern).
- Audio response plays automatically after each exchange.
- No complex UI. No onboarding screens. Open → speak → hear. That's it.
- Designed so a completely illiterate user can operate it without reading anything.

### 2. Native Conversation Engine

- Understands Hinglish naturally — code-switching mid-sentence is expected, not an edge case.
- Reads indirect emotion. 'Kuch acha nahi lag raha aajkal' = loneliness. No explicit label needed.
- Responds with cultural warmth — uses 'beta', 'aap', 'accha sunao', 'aye bhai' contextually.
- Never clinical, never rushed, never condescending. One question at a time.
- Dynamic System prompt is the soul — iterated obsessively in prompts.py. — Clarity Needed

### 3. Session Memory + Emotional Connect

- Maintains full conversation history within the session via st.session_state.
- References earlier statements naturally — 'Aapne abhi bataya ki...'
- Basic emotional thread tracking — detects tonal shifts and responds to them.
- 10–15 hardcoded 'oral moments' — dohas, short kahaniyan — triggered by emotional context.

---

## V2 — Build the Soul (Post-validation)

Once apnapan is confirmed, build the layers that make it irreplaceable.

### 1. Persistent Memory Across Sessions

- User profile built over weeks — interests, recurring themes, emotional patterns.
- Stored locally. Never leaves the device. Privacy by architecture, not policy.
- 'Aap har Sunday ko thoda udaas lagte ho' — this kind of longitudinal awareness.

### 2. Expanded Oral Tradition Library

- 100+ oral moments — kahavat, lok geet references, kahaniyan, kimvidantiye — mapped to emotional contexts.
- Categorised by emotion: grief, confusion, longing, pride, hope, uncertainty.
- Curated from actual Indian oral tradition — not generated. Each one chosen deliberately.

### 3. Multilingual Support

- Bhashini integration for regional languages — Punjabi, Bengali, Tamil, Marathi, etc.
- AI4Bharat IndicTrans2 for cross-language comprehension.
- Same soul, many tongues.

---

## V3 — Build the Bridge (The Full Vision)

The intergenerational connection that makes AGELESS unlike anything that exists.

### 1. The Story Archive

- Elders contribute stories — anonymised, with explicit consent.
- Stories tagged by theme: career change, loss, resilience, starting over, family, social prejudice, etc.
- Not a database. A living oral archive, recounting lived wisdom.

### 3. The Bridge

- When a young user faces a specific struggle, AGELESS surfaces a relevant elder's story.
- Not as advice. As narrative. 'Ek baat sunao...'
- The elder never knows their story reached someone. The youth never knows it came from a real person. The bridge is invisible. That's the design.

### 4. Self-Hosted / Frontier Model

- Migrate from Sarvam APIs to self-hosted AI4Bharat models — IndicWav2Vec, IndicBERT.
- Eventually: fine-tune & train own model specifically on Indian conversational, emotional, oral data.
- Compute via C-DAC Param infrastructure. Fully sovereign. No external API dependency.

---

## ◆ SECTION 04

# Tech Architecture

## V1 Stack — Indian-First, Sovereign by Design

Every layer of the stack is Indian. This is not a coincidence. It is a design decision.

| **Layer** | **Tool / Model** | **Why** |
|---|---|---|
| **UI** | Streamlit | Browser-based, no install, accessible, voice-first possible |
| **Mic Capture** | streamlit-mic-recorder | Browser mic access without native app |
| **Speech-to-Text** | Sarvam Saarika | Hindi-first, Indian accents, REST API |
| **LLM** | Sarvam-1 | Hinglish native, Indian cultural context built in |
| **Text-to-Speech** | Sarvam Bulbul | Natural Hindi voice — sounds human |
| **Memory** | st.session_state | In-session history, zero infra needed for v1 |
| **Secrets** | .env + python-dotenv | API keys never hardcoded |

## Project File Structure —

```
ageless/
    app.py            # streamlit entry point
    stt.py            # Saarika STT API wrapper
    llm.py            # Sarvam-1 + conversation logic
    tts.py            # Bulbul TTS API wrapper
    prompts.py        # THE SOUL — system prompt versions
    oral_library.py   # dohas, kahaniyan, oral moments
    config.py         # language settings, constants
    .env              # secrets — NEVER commit
    requirements.txt
```

---

## ◆ SECTION 05

# Success Metrics & KPIs

## The Only Metric That Matters First

> Before any number — does it make one person say 'yeh toh apna lag raha hai'? If not, nothing else counts.

## V1 Metrics — Feel & Function

| **Metric** | **Target** | **Signal** |
|---|---|---|
| **Apnapan response** | 1 of first 5 users | Unprompted emotional resonance |
| **Session length** | > 10 minutes | User didn't want to stop |
| **Voice usage rate** | > 60% of inputs | Confirming voice-first hypothesis |
| **STT accuracy (Hindi)** | > 85% | Conversations not breaking due to transcription |
| **Oral moment landing** | 1 per session felt relevant | User pauses, reflects, or reacts |
| **Return usage** | Same user returns once | Product created pull, not just novelty |

## V2 Metrics — Memory & Depth

| **Metric** | **Target** | **Signal** |
|---|---|---|
| **Weekly active return** | > 3 sessions / week | Habit forming, not novelty |
| **Memory accuracy** | User confirms recall | 'Haan, maine yeh bataya tha' |
| **Emotional pattern detection** | 1 pattern per 2 weeks | AGELESS notices what user doesn't say |
| **Language coverage** | 3+ Indian languages | Beyond Hindi-only |

---

## ◆ SECTION 06

# Risks & Mitigations

| **Risk** | **Level** | **Mitigation** |
|---|---|---|
| **Sarvam API goes down or changes pricing — The API Wrapper Delima** | **High** | Design stt.py, llm.py, tts.py as swappable modules. Bhashini as fallback. AI4Bharat for self-hosting path. |
| **STT accuracy poor for elderly speech (slower, accented)** | **High** | Test early with real elderly users. Fine-tune prompts to handle partial transcription gracefully. |
| **System prompt produces clinical / cold responses** | **High** | prompts.py is a living file. Iterate after every user session. Never ship a prompt untested with a real human. |
| **Users feel uncomfortable talking to a machine** | **Medium** | Don't hide that it's AI. But don't lead with it either. Let the warmth speak first. Consent by experience. |
| **Oral moments feel forced or irrelevant** | **Medium** | Hardcode conservatively. 10 very good moments beat 50 mediocre ones. Test each one individually. |
| **Privacy concerns with emotional data** | **Low (v1)** | v1 has no persistence. Session data dies on close. Document this clearly for users. |

---

## A Note to Myself

This PRD exists not to impress anyone. It exists so that on the days when the code doesn't work, when the API returns an error, when a test session feels flat — I have something to come back to that reminds me what I am actually building and why.

The soul of this project is not in this document. The soul is in prompts.py. It is in the moment a 68-year-old woman talks for an hour and doesn't notice the time. It is in the moment a 24-year-old hears a stranger's story and feels less alone.

Build that. Everything else is just scaffolding.

---

**NOTE:-** Ageless **MUST NOT** be **API Wrapper**, it should be built from ground up, sovereign, ingenious & really innovative by design...Some ground breaking work must be done.

---
*— AGELESS Companion · Anshuman's First Build · Ghaziabad · Feb 2026*
