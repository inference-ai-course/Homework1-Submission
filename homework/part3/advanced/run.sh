#!/bin/bash

# Quick Launch Script for AI Proxy Agent
# =======================================

echo "======================================================================"
echo "  AI Proxy Agent - Gradio Web Interface"
echo "  "
echo "  Author: Christine Zhao"
echo "  Version: 1.0.0"
echo "  Created: 2025-10-25"
echo "======================================================================"
echo ""

# Check if Ollama is running
echo "Checking Ollama status..."
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "✓ Ollama is running"
    echo ""
    echo "Available models:"
    curl -s http://localhost:11434/api/tags | grep -o '"name":"[^"]*"' | cut -d'"' -f4 | head -5
    echo ""
else
    echo "✗ Ollama is not running!"
    echo ""
    echo "Please start Ollama:"
    echo "  $ ollama serve"
    echo ""
    echo "Or check if Ollama is installed:"
    echo "  $ ollama --version"
    echo ""
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source ../../../venv/bin/activate

# Check dependencies
echo "Checking Python dependencies..."
if python -c "import gradio, langchain_community, openai" 2>/dev/null; then
    echo "✓ All dependencies installed"
else
    echo "✗ Missing dependencies!"
    echo ""
    echo "Installing required packages..."
    pip install gradio langchain-community langchain-core langchain-ollama openai
fi

echo ""
echo "======================================================================"
echo "Starting Gradio interface..."
echo "======================================================================"
echo ""
echo "The interface will be available at: http://127.0.0.1:7860"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Launch the application
python gradio_ai_proxy.py