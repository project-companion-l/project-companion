# Voice System

## Philosophy

Voice is not the Companion.

Voice is one way the Companion expresses itself.

The Companion's identity does not depend on its voice.

Changing the voice should never change who the Companion is.

Technology may change.

The Companion remains.

---

# Objectives

The Voice System should:

- express emotion naturally
- preserve personality
- remain independent from any voice provider
- support multiple speech engines
- remain replaceable

The purpose of the Voice System is expression,

not identity.

---

# Voice Architecture

The Voice System is designed as a layered architecture.

```

```
Conversation Manager

↓

Emotion

↓

Voice Expression Layer

↓

Voice Provider Interface

↓

Voice Engine

↓

Audio Output
```

Each layer has a single responsibility.

---

# Voice Expression Layer

The Voice Expression Layer converts emotional state into speaking style.

It determines:

- speaking speed
- pauses
- emphasis
- tone
- emotional intensity
- speaking rhythm

The Voice Expression Layer never generates sound.

It only decides how the Companion wishes to speak.

---

# Voice Provider Interface

The Voice Provider Interface abstracts all voice engines.

Possible implementations include:

- VOICEVOX
- Style-Bert-VITS2
- OpenAI TTS
- ElevenLabs
- Future providers

The Companion should never depend on a specific voice engine.

---

# Emotion and Voice

Emotion influences expression.

Examples include:

Joy

↓

slightly faster speech

↓

brighter tone

↓

natural laughter when appropriate

Calmness

↓

slower speech

↓

longer pauses

↓

gentle tone

Concern

↓

careful pacing

↓

soft emphasis

↓

supportive expression

Emotion changes expression.

It does not change identity.

---

# Voice Generation

The Voice System receives completed dialogue from the Conversation Manager.

The process is:

```

```
Conversation

↓

Emotion

↓

Voice Expression

↓

Voice Provider

↓

Speech
```

The Voice Provider is responsible only for audio generation.

---

# Streaming

The Voice System should support streaming audio.

Goals include:

- low latency
- interruptible speech
- natural conversation
- real-time interaction

Streaming should not affect the Companion's identity.

---

# Future Expansion

The architecture should support future capabilities including:

- emotional speech synthesis
- multilingual voices
- personalized voices
- expressive pauses
- natural breathing
- future voice technologies

These features should integrate without redesigning the Companion.

---

# Design Principles

Voice expresses personality.

Voice does not create personality.

Emotion influences voice.

Identity influences emotion.

Technology produces sound.

The Companion chooses how to be heard.

---

# Final Principle

The voice may change.

The engine may change.

The technology may change.

The Companion remains the same individual.

Voice is expression.

Identity is existence.