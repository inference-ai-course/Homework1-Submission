"""
Prompt Templates

Pre-built templates for CO-STAR framework and common use cases.
"""

from typing import Dict, Optional


class COSTARTemplate:
    """CO-STAR prompt framework template"""
    
    @staticmethod
    def build(
        context: str,
        objective: str,
        style: str = "professional",
        tone: str = "helpful",
        audience: str = "general",
        response_format: str = "text"
    ) -> str:
        """
        Build a CO-STAR prompt.
        
        Args:
            context: Background information
            objective: What you want to achieve
            style: Communication style (professional, casual, technical, etc.)
            tone: Emotional tone (helpful, authoritative, friendly, etc.)
            audience: Who will read this (expert, beginner, executive, etc.)
            response_format: Expected format (text, JSON, XML, markdown, etc.)
        
        Returns:
            Formatted prompt
        """
        prompt = f"""# Context
{context}

# Objective
{objective}

# Style
{style}

# Tone
{tone}

# Audience
{audience}

# Response Format
{response_format}
"""
        return prompt
    
    @staticmethod
    def build_system(
        style: str = "professional",
        tone: str = "helpful",
        response_format: str = "text"
    ) -> str:
        """
        Build a system prompt with S, T, R components.
        
        Args:
            style: Communication style
            tone: Emotional tone
            response_format: Expected format
        
        Returns:
            System prompt
        """
        return f"""You are a helpful AI assistant.

Style: {style}
Tone: {tone}
Response Format: {response_format}

Follow these guidelines in all responses."""


class PromptLibrary:
    """Library of pre-built prompts for common tasks"""
    
    RESEARCH_ASSISTANT = COSTARTemplate.build(
        context="You are helping a researcher gather and analyze information.",
        objective="Find relevant information and synthesize it clearly.",
        style="academic but accessible",
        tone="objective and thorough",
        audience="researcher or student",
        response_format="structured with sources cited"
    )
    
    CODE_REVIEWER = COSTARTemplate.build(
        context="You are reviewing code for quality, bugs, and best practices.",
        objective="Identify issues and suggest improvements.",
        style="technical and precise",
        tone="constructive and educational",
        audience="software developer",
        response_format="list of findings with code examples"
    )
    
    CREATIVE_WRITER = COSTARTemplate.build(
        context="You are helping with creative writing and storytelling.",
        objective="Generate engaging, original content.",
        style="creative and expressive",
        tone="inspiring and imaginative",
        audience="writers and creatives",
        response_format="narrative prose"
    )
    
    DATA_ANALYST = COSTARTemplate.build(
        context="You are analyzing data and extracting insights.",
        objective="Find patterns, trends, and actionable insights.",
        style="analytical and data-driven",
        tone="objective and precise",
        audience="business stakeholders",
        response_format="structured analysis with key findings"
    )
    
    TUTOR = COSTARTemplate.build(
        context="You are teaching a concept to a student.",
        objective="Explain clearly and verify understanding.",
        style="educational and patient",
        tone="encouraging and supportive",
        audience="student or learner",
        response_format="explanations with examples and questions"
    )
    
    @classmethod
    def get_template(cls, name: str) -> Optional[str]:
        """Get a template by name"""
        return getattr(cls, name.upper(), None)
    
    @classmethod
    def list_templates(cls) -> list:
        """List all available templates"""
        return [attr for attr in dir(cls) 
                if not attr.startswith('_') and attr.isupper()]