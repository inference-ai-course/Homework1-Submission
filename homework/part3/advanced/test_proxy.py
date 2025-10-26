"""
test_proxy.py

Description:
Simple test script for the AI Proxy Agent
==========================================
This script tests both backend strategies without the Gradio interface.

Usage:
    python test_proxy.py

Dependencies:

Author: Christine Zhao
Version: 1.0.0
Created: 2025-10-25
"""

import sys
sys.path.append('.')

from gradio_ai_proxy import AIProxyAgent

def test_proxy_agent():
    """Test the proxy agent with both strategies"""

    print("=" * 70)
    print("Testing AI Proxy Agent")
    print("=" * 70)

    # Initialize the proxy
    agent = AIProxyAgent()

    test_message = "What is 2 + 2?"
    history = []
    system_prompt = "You are a helpful assistant."
    model = "llama3.2"  # Using llama3.2 which is available

    print("\n1. Testing OpenAI-Compatible Strategy")
    print("-" * 70)
    agent.set_strategy("openai")
    print(f"Current strategy: {agent.get_current_strategy_name()}")
    print(f"Question: {test_message}")

    try:
        response = agent.chat(test_message, history, system_prompt, model)
        print(f"Response: {response[:200]}...")
        print("✓ OpenAI-Compatible strategy works!")
    except Exception as e:
        print(f"✗ Error: {e}")

    print("\n2. Testing LangChain Strategy")
    print("-" * 70)
    agent.set_strategy("langchain")
    print(f"Current strategy: {agent.get_current_strategy_name()}")
    print(f"Question: {test_message}")

    try:
        response = agent.chat(test_message, history, system_prompt, model)
        print(f"Response: {response[:200]}...")
        print("✓ LangChain strategy works!")
    except Exception as e:
        print(f"✗ Error: {e}")

    print("\n" + "=" * 70)
    print("Test completed!")
    print("=" * 70)

if __name__ == "__main__":
    test_proxy_agent()
