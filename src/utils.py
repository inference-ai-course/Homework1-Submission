"""
Utility Functions

Helper functions for token estimation, cost calculation, and formatting.
"""

from typing import Dict, Any, Optional



def estimate_tokens(text: str) -> int:
    """
    Rough estimation of tokens.
    Rule of thumb: 1 token ≈ 4 characters in English
    
    Args:
        text: Text to estimate
    
    Returns:
        Estimated token count
    """
    return len(text) // 4


def estimate_cost(
    input_text: str,
    output_tokens: int,
    model: str = "claude-sonnet-4-5-20250929"
) -> float:
    """
    Estimate API call cost.
    
    Args:
        input_text: Your prompt
        output_tokens: Expected response length
        model: Model to use
    
    Returns:
        Estimated cost in dollars
    """
    pricing = {
        "claude-sonnet-4-5-20250929": {"input": 3.0, "output": 15.0},
        "claude-opus-4-5-20251101": {"input": 15.0, "output": 75.0},
        "claude-haiku-4-5-20251001": {"input": 1.0, "output": 5.0},
    }
    
    if model not in pricing:
        model = "claude-sonnet-4-5-20250929"  # Default
    
    input_tokens = estimate_tokens(input_text)
    
    input_cost = (input_tokens / 1_000_000) * pricing[model]['input']
    output_cost = (output_tokens / 1_000_000) * pricing[model]['output']
    
    return input_cost + output_cost


def format_response(response: Dict[str, Any], verbose: bool = True) -> str:
    """
    Format an LLM response for display.
    
    Args:
        response: Response from LLMClient.generate()
        verbose: If True, include metadata
    
    Returns:
        Formatted string
    """
    if "error" in response:
        return f"❌ Error: {response['error']}"
    
    output = []
    
    if verbose:
        output.append("=" * 60)
        output.append(f"Model: {response['model']}")
        output.append(f"Tokens: {response['usage']['input_tokens']} in, "
                     f"{response['usage']['output_tokens']} out")
        output.append(f"Stop reason: {response['stop_reason']}")
        output.append("=" * 60)
    
    output.append(response['content'])
    
    if verbose:
        output.append("=" * 60)
    
    return "\n".join(output)


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to maximum length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
    
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def count_words(text: str) -> int:
    """Count words in text"""
    return len(text.split())


def calculate_savings(verbose_tokens: int, concise_tokens: int, model: str = "claude-sonnet-4-5-20250929") -> Dict[str, Any]:
    """
    Calculate savings from using concise prompts.
    
    Args:
        verbose_tokens: Token count for verbose version
        concise_tokens: Token count for concise version
        model: Model being used
    
    Returns:
        Dictionary with savings information
    """
    pricing = {
        "claude-sonnet-4-5-20250929": {"input": 3.0, "output": 15.0},
        "claude-opus-4-5-20251101": {"input": 15.0, "output": 75.0},
        "claude-haiku-4-5-20251001": {"input": 1.0, "output": 5.0},
    }
    
    if model not in pricing:
        model = "claude-sonnet-4-5-20250929"
    
    token_savings = verbose_tokens - concise_tokens
    token_savings_pct = (token_savings / verbose_tokens * 100) if verbose_tokens > 0 else 0
    
    cost_per_token = pricing[model]['input'] / 1_000_000
    cost_savings = token_savings * cost_per_token
    
    return {
        "token_savings": token_savings,
        "token_savings_percent": token_savings_pct,
        "cost_savings": cost_savings,
        "verbose_tokens": verbose_tokens,
        "concise_tokens": concise_tokens
    }

def save_task_output(
    task_name: str,
    notebook: str,
    prompt: str,
    response: Dict[str, Any],
    system_prompt: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    observations: Optional[str] = None,
    output_dir: str = None
) -> str:
    """
    Save task output to markdown file.
    
    Args:
        task_name: Name of the task (e.g., "Task 1: Custom System Prompt")
        notebook: Notebook number (e.g., "02")
        prompt: User prompt used
        response: Response from LLMClient.generate()
        system_prompt: System prompt if used
        metadata: Additional metadata to include
        observations: Student observations/reflections
        output_dir: Directory to save to (default: outputs/)
    
    Returns:
        Path to saved file
    """
    from datetime import datetime  # ✅ Import here
    import os
    from typing import Dict, Any, Optional
    
    if output_dir is None:
        output_dir = 'outputs'
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Build markdown content
    content = [
        f"# {task_name}",
        "",
        f"**Notebook:** {notebook}  ",
        f"**Completed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]
    
    # System prompt section
    if system_prompt:
        content.extend([
            "## System Prompt",
            "",
            "```",
            system_prompt.strip(),
            "```",
            "",
        ])
    
    # User prompt section
    content.extend([
        "## User Prompt",
        "",
        "```",
        prompt.strip(),
        "```",
        "",
    ])
    
    # Response section
    if "error" in response:
        content.extend([
            "## Response",
            "",
            f"❌ **Error:** {response['error']}",
            "",
        ])
    else:
        content.extend([
            "## Response",
            "",
            response['content'],
            "",
        ])
    
    # Metadata section
    if "error" not in response:
        content.extend([
            "## Metadata",
            "",
            f"- **Model:** {response['model']}",
            f"- **Input tokens:** {response['usage']['input_tokens']:,}",
            f"- **Output tokens:** {response['usage']['output_tokens']:,}",
            f"- **Total tokens:** {response['usage']['input_tokens'] + response['usage']['output_tokens']:,}",
        ])
        
        if metadata:
            for key, value in metadata.items():
                content.append(f"- **{key.replace('_', ' ').title()}:** {value}")
        
        content.append("")
    
    # Observations section
    if observations:
        content.extend([
            "## Your Observations",
            "",
            observations.strip(),
            "",
        ])
    
    content.append("---")
    
    # Generate filename
    task_slug = task_name.lower().replace(' ', '_').replace(':', '').replace('#', '')
    task_slug = ''.join(c for c in task_slug if c.isalnum() or c == '_')
    filename = f"notebook{notebook}_{task_slug}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    
    return filepath