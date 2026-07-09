"""
Configuration management for Project Companion.
"""

from dataclasses import dataclass


@dataclass
class Config:
    """Application configuration."""

    app_name: str = "Project Companion"

    debug: bool = True

    llm_provider: str = "none"

    memory_enabled: bool = False

    voice_enabled: bool = False