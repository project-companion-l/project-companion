# Conversation Flow

Version: 1.0

Status: Draft

---

# Purpose

This document defines how conversations are processed inside Project Companion.

The goal is to ensure that every response is generated consistently, regardless of the AI provider or voice engine.

Conversation is not a simple question-and-answer process.

Every interaction is influenced by personality, memories, and the relationship between the user and the Companion.

---

# Conversation Pipeline

User Input

↓

Input Processing

↓

Conversation Context

↓

Memory Retrieval

↓

Identity Reflection

↓

AI Reasoning

↓

Response Generation

↓

Memory Update

↓

Output Generation

↓

User

---

# 1. User Input

Project Companion supports multiple input methods.

Supported inputs:

- Voice
- Text
- Future external APIs

The conversation engine treats all inputs identically after preprocessing.

---

# 2. Input Processing

Responsibilities:

- Speech-to-Text (if voice)
- Text normalization
- Language detection (future)
- Command detection
- Metadata generation

Metadata examples:

- Timestamp
- Device
- Conversation ID

---

# 3. Conversation Context

The system constructs the current conversation context.

Context includes:

- Current user message
- Previous conversation
- Current session
- Active tasks
- Current emotional context

---

# 4. Memory Retrieval

The Memory Engine searches relevant memories.

Search order:

1. Short-Term Memory
2. Relationship Memory
3. Profile Memory
4. Long-Term Memory

Only relevant memories are returned.

---

# 5. Identity Reflection

Before asking the AI to respond,
the Identity Layer determines:

- Personality
- Speaking style
- Core values
- Emotional tendencies
- Current relationship status

Identity remains independent from the AI provider.

---

# 6. AI Reasoning

The AI Provider receives:

- Conversation context
- Retrieved memories
- Identity information

The provider generates a candidate response.

The provider does not permanently store memories.

---

# 7. Response Generation

The Conversation Engine reviews the response.

Responsibilities include:

- Tone adjustment
- Safety checks
- Personality consistency
- Emotional consistency
- Command execution (future)

---

# 8. Memory Update

After the response is finalized,
the Memory Engine determines what should be stored.

Possible actions:

- Update Short-Term Memory
- Store Long-Term Memory
- Update Relationship Memory
- Ignore temporary information

Memory updates should be selective.

Not every conversation becomes a permanent memory.

---

# 9. Output Generation

The response is converted into the requested output format.

Supported outputs:

- Text
- Voice
- Future animation
- Future avatar expressions

Voice generation should not affect conversation logic.

---

# Error Handling

If one subsystem fails:

- AI unavailable
- Voice generation failure
- Memory lookup failure

The system should degrade gracefully.

Conversation should continue whenever possible.

---

# Design Principles

- Conversation is context-aware.
- Identity is persistent.
- Memory is selective.
- AI providers are replaceable.
- Voice systems are independent.
- Every interaction strengthens the relationship between the user and the Companion.