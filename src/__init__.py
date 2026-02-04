"""
Week 1: LLM Introduction - Shared Modules

This package contains reusable code for all notebooks.
"""

__version__ = "1.0.0"

from .llm_client import LLMClient
from .cost_tracker import CostTracker
from .utils import estimate_tokens, estimate_cost, format_response, save_task_output

__all__ = [
    'LLMClient',
    'CostTracker',
    'estimate_tokens',
    'estimate_cost',
    'format_response',
    'save_task_output'
]