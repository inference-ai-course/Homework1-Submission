# Task 1: Custom System Prompt

**Notebook:** 02  
**Completed:** 2026-02-04 01:11:56

## System Prompt

```
# YOUR SYSTEM PROMPT HERE

Example:
You are a professional code reviewer with expertise in Python.
You provide constructive feedback, identify bugs, and suggest improvements.
Be thorough but concise. Focus on: correctness, efficiency, and readability.
```

## User Prompt

```
# YOUR USER PROMPT HERE

Example:
Review this Python function:
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

## Response

# Code Review: `calculate_average` Function

## Overview
This function calculates the arithmetic mean of a list of numbers. While functionally correct for the happy path, it lacks error handling and could benefit from improvements.

## Issues Identified

### 1. **Critical: No Error Handling for Empty List**
```python
calculate_average([])  # ZeroDivisionError: division by zero
```
**Impact**: The function will crash when given an empty list.

### 2. **No Input Validation**
- No type checking for the `numbers` parameter
- Could fail with non-numeric values in unexpected ways

### 3. **Missing Documentation**
- No docstring explaining purpose, parameters, or return value

## Suggested Improvements

```python
def calculate_average(numbers):
    """
    Calculate the arithmetic mean of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values (int or float)
        
    Returns:
        float: The average of the numbers
        
    Raises:
        ValueError: If the list is empty
        TypeError: If numbers contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    
    return sum(numbers) / len(numbers)
```

## Alternative Considerations

## Metadata

- **Model:** claude-sonnet-4-5-20250929
- **Input tokens:** 101
- **Output tokens:** 300
- **Total tokens:** 401
- **Temperature:** 0.7
- **Max Tokens:** 300

## Your Observations

What I learned from this task:
- [Your observation here]

How the system prompt affected the response:
- [Your observation here]

Potential real-world applications:
- [Your observation here]

---