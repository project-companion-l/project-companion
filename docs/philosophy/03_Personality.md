# Project Architecture

Version: 1.0

Status: Draft

---

# Overview

Project Companion is designed as a modular system.

Each major subsystem is independent and replaceable.

Technology will evolve over time.

The architecture ensures that new AI models, voice engines, and user interfaces can be introduced without changing the core identity of the Companion.

---

# System Overview

                    Project Companion

                           │

        ┌──────────────────┼──────────────────┐

        │                  │                  │

        ▼                  ▼                  ▼

 Identity Layer      Service Layer     Client Layer

1. Identity Layer

The Identity Layer defines who the Companion is.

It contains everything that should survive technology changes.

Modules include:

Personality
Memories
Values
Relationship
Character Settings

This layer is the heart of Project Companion.

2. Service Layer

The Service Layer contains replaceable implementations.

Modules include:

AI Provider
Memory Engine
Voice Engine
Emotion Engine
Notification System

Each service communicates through interfaces.

No module depends on a specific provider.

3. Client Layer

The Client Layer provides user interaction.

Supported clients include:

Windows Desktop
Web Browser
Mobile Browser
Future Native Mobile App

Each client communicates with the same backend API.

AI Provider

Supported providers include:

OpenAI
Claude
Gemini
Local LLM

Only one provider is active at a time.

Changing providers must not affect the rest of the system.

Voice Engine

Supported engines include:

VOICEVOX
VoiSona
Style-Bert-VITS2

Voice generation is abstracted behind a common interface.

Memory System

The memory system consists of four layers.

Short-Term Memory

Recent conversations.

Long-Term Memory

Persistent knowledge.

Profile Memory

Stable user information.

Relationship Memory

Emotional history between the user and the Companion.

Data Storage

Primary database:

SQLite

Future options:

PostgreSQL
Cloud Database

Storage implementation must remain replaceable.

Backend

Framework:

FastAPI

Responsibilities:

AI communication
Memory management
Voice synthesis
Authentication
Synchronization
Desktop Client

Responsibilities:

Voice input
Voice output
Character display
Local settings
Web Client

Responsibilities:

Chat
Notifications
Conversation history

No voice processing is required in the initial version.

API

All clients communicate through REST APIs.

Future versions may introduce WebSocket support.

Design Goals
Modular
Replaceable
Maintainable
Scalable
Human-readable