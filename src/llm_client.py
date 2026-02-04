"""
Unified LLM Client for Claude API and Ollama

This module provides a single interface for interacting with both
cloud-based (Claude) and local (Ollama) language models.
"""

import os
import requests
from typing import Dict, List, Optional, Any


class LLMClient:
    """Unified client for interacting with LLMs (Claude or Ollama)"""
    
    def __init__(self, path: str = "A"):
        """
        Initialize the LLM client based on chosen path.
        
        Args:
            path: "A" for Claude, "B" for Ollama, "C" for Hybrid
        """
        self.path = path
        self.claude_client = None
        self.default_model = None
        
        # Initialize based on path
        if path in ["A", "C"]:
            self._init_claude()
        if path in ["B", "C"]:
            self._init_ollama()
    
    def _init_claude(self):
        """Initialize Claude API client"""
        try:
            import anthropic
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY not found in environment")
            
            self.claude_client = anthropic.Anthropic(api_key=api_key)
            
            # Claude 4.5 model names
            self.default_model = "claude-sonnet-4-5-20250929"
            
            print("✓ Claude API client initialized")
            print(f"  Default model: {self.default_model}")
            print(f"  Available: Opus 4.5, Sonnet 4.5, Haiku 4.5")
        except Exception as e:
            print(f"❌ Failed to initialize Claude: {e}")
            raise
    
    def _init_ollama(self):
        """Initialize Ollama client"""
        try:
            # Test if Ollama is running
            response = requests.get('http://localhost:11434/api/tags', timeout=5)
            if response.status_code == 200:
                models = response.json().get('models', [])
                if models:
                    self.default_model = models[0]['name']
                    print("✓ Ollama client initialized")
                    print(f"  Available models: {[m['name'] for m in models]}")
                    print(f"  Default model: {self.default_model}")
                else:
                    print("⚠ Ollama running but no models found")
                    print("  Run: ollama pull llama3.2:3b")
            else:
                print("❌ Ollama not responding")
                raise ConnectionError("Ollama server not responding")
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to connect to Ollama: {e}")
            print("  Make sure Ollama is running: ollama serve")
            raise
    
    def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        model: Optional[str] = None,
        temperature: float = 1.0,
        max_tokens: int = 1024,
        use_claude: bool = None
    ) -> Dict[str, Any]:
        """
        Generate a response from the LLM.
        
        Args:
            prompt: The user prompt
            system: System prompt (optional)
            model: Override default model
            temperature: Randomness (0-1 for Claude, 0-2 for Ollama)
            max_tokens: Maximum response length
            use_claude: For hybrid path, explicitly choose Claude
        
        Returns:
            Dictionary with 'content', 'model', 'usage' keys
        """
        # Determine which backend to use
        use_claude_backend = False
        if self.path == "A":
            use_claude_backend = True
        elif self.path == "B":
            use_claude_backend = False
        elif self.path == "C":  # Hybrid
            use_claude_backend = use_claude if use_claude is not None else False
        
        # Select model if not specified
        if model is None:
            model = self.default_model
        
        # Generate response
        if use_claude_backend:
            return self._generate_claude(prompt, system, model, temperature, max_tokens)
        else:
            return self._generate_ollama(prompt, system, model, temperature, max_tokens)
    
    def _generate_claude(
        self,
        prompt: str,
        system: Optional[str],
        model: str,
        temperature: float,
        max_tokens: int
    ) -> Dict[str, Any]:
        """Generate response using Claude API"""
        try:
            messages = [{"role": "user", "content": prompt}]
            
            kwargs = {
                "model": model,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature
            }
            
            if system:
                kwargs["system"] = system
            
            response = self.claude_client.messages.create(**kwargs)
            
            return {
                "content": response.content[0].text,
                "model": response.model,
                "usage": {
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens
                },
                "stop_reason": response.stop_reason
            }
        except Exception as e:
            return {"error": str(e), "model": model}
    
    def _generate_ollama(
        self,
        prompt: str,
        system: Optional[str],
        model: str,
        temperature: float,
        max_tokens: int
    ) -> Dict[str, Any]:
        """Generate response using Ollama"""
        try:
            # Combine system and user prompt for Ollama
            full_prompt = prompt
            if system:
                full_prompt = f"{system}\n\n{prompt}"
            
            # Make request to Ollama API
            response = requests.post(
                'http://localhost:11434/api/generate',
                json={
                    "model": model,
                    "prompt": full_prompt,
                    "temperature": temperature,
                    "stream": False,
                    "options": {
                        "num_predict": max_tokens
                    }
                },
                timeout=120  # 2 minute timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "content": data['response'],
                    "model": model,
                    "usage": {
                        "input_tokens": data.get('prompt_eval_count', 0),
                        "output_tokens": data.get('eval_count', 0)
                    },
                    "stop_reason": "complete"
                }
            else:
                return {"error": f"HTTP {response.status_code}", "model": model}
                
        except Exception as e:
            return {"error": str(e), "model": model}
    
    def get_available_models(self) -> List[str]:
        """Get list of available models"""
        models = []
        
        if self.path in ["A", "C"]:
            models.extend([
                "claude-sonnet-4-5-20250929",
                "claude-opus-4-5-20251101",
                "claude-haiku-4-5-20251001"
            ])
        
        if self.path in ["B", "C"]:
            try:
                response = requests.get('http://localhost:11434/api/tags', timeout=5)
                if response.status_code == 200:
                    ollama_models = [m['name'] for m in response.json().get('models', [])]
                    models.extend(ollama_models)
            except:
                pass
        
        return models