import gradio as gr
from langchain_community.llms import Ollama
from datetime import datetime
import json

class SimpleAIAgent:
    """Simple AI Agent using Ollama directly - no chains or memory modules"""
    
    def __init__(self, model_name="llama2", temperature=0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.llm = Ollama(model=model_name, temperature=temperature)
        self.chat_history = []
        self.chat_logs = []
        print(f"✓ Initialized with model: {model_name}")
    
    def chat(self, message, system_prompt=None):
        """Simple chat with history"""
        try:
            # Build prompt with history
            prompt = ""
            
            if system_prompt and system_prompt.strip():
                prompt += f"System: {system_prompt}\n\n"
            
            # Add recent history (last 5 exchanges to keep context)
            for hist in self.chat_history[-5:]:
                prompt += f"User: {hist['user']}\nAssistant: {hist['assistant']}\n\n"
            
            prompt += f"User: {message}\nAssistant:"
            
            # Get response from Ollama
            response = self.llm.invoke(prompt)
            
            # Save to history
            self.chat_history.append({
                "user": message,
                "assistant": response
            })
            
            # Log with timestamp
            self.chat_logs.append({
                "timestamp": datetime.now().isoformat(),
                "user": message,
                "assistant": response
            })
            
            return response
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}\n\n"
            error_msg += "Troubleshooting:\n"
            error_msg += "1. Make sure Ollama is running: ollama serve\n"
            error_msg += f"2. Make sure model is available: ollama pull {self.model_name}\n"
            error_msg += "3. Test Ollama: ollama run llama2 'hello'"
            return error_msg
    
    def clear(self):
        """Clear chat history"""
        self.chat_history = []
        self.chat_logs = []
    
    def get_stats(self):
        """Get chat statistics"""
        if not self.chat_logs:
            return "📊 **Statistics**: No messages yet"
        
        return f"""📊 **Chat Statistics**
- Total messages: {len(self.chat_logs)}
- Model: {self.model_name}
- Temperature: {self.temperature}
- Started: {self.chat_logs[0]['timestamp']}
"""
    
    def export(self):
        """Export chat history to JSON"""
        if not self.chat_logs:
            return "⚠️ No chat to export"
        
        filename = f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.chat_logs, f, indent=2, ensure_ascii=False)
            return f"✓ Chat exported to {filename}"
        except Exception as e:
            return f"❌ Export failed: {str(e)}"

# Initialize agent
print("="*80)
print("Initializing AI Agent...")
print("="*80)
agent = SimpleAIAgent(model_name="llama2", temperature=0.7)

# Gradio interface functions
def chat_function(message, history, system_prompt):
    """Handle chat messages"""
    if not message.strip():
        return history, ""
    
    response = agent.chat(message, system_prompt)
    history.append((message, response))
    return history, ""

def clear_function():
    """Clear chat"""
    agent.clear()
    return None, "✓ Chat cleared!"

def stats_function():
    """Get statistics"""
    return agent.get_stats()

def export_function():
    """Export chat"""
    return agent.export()

# Create Gradio interface
with gr.Blocks(title="AI Agent Proxy", theme=gr.themes.Soft()) as app:
    
    gr.Markdown(
        """
        # 🤖 AI Agent Proxy Interface
        ## Ollama + LangChain + Gradio Integration
        
        Chat with a local AI model powered by Ollama with conversation memory and export capabilities.
        """
    )
    
    with gr.Row():
        # Left column - Chat interface
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                label="💬 Chat with AI Agent",
                height=500,
                avatar_images=(None, "🤖"),
                show_label=True
            )
            
            with gr.Row():
                message_input = gr.Textbox(
                    label="Your Message",
                    placeholder="Type your message here...",
                    lines=2,
                    scale=4
                )
                send_button = gr.Button("Send 📤", variant="primary", scale=1)
            
            with gr.Accordion("⚙️ Advanced Options", open=False):
                system_prompt_input = gr.Textbox(
                    label="System Prompt (Optional)",
                    placeholder="e.g., You are a helpful Python coding assistant who provides clear examples...",
                    lines=3
                )
        
        # Right column - Controls
        with gr.Column(scale=1):
            gr.Markdown("### 🎮 Controls")
            
            clear_button = gr.Button("🗑️ Clear Chat", variant="secondary", size="sm")
            stats_button = gr.Button("📊 Statistics", variant="secondary", size="sm")
            export_button = gr.Button("💾 Export Chat", variant="secondary", size="sm")
            
            status_box = gr.Textbox(
                label="Status",
                value="Ready ✓",
                interactive=False,
                lines=4
            )
    
    # Event handlers
    message_input.submit(
        chat_function,
        inputs=[message_input, chatbot, system_prompt_input],
        outputs=[chatbot, message_input]
    )
    
    send_button.click(
        chat_function,
        inputs=[message_input, chatbot, system_prompt_input],
        outputs=[chatbot, message_input]
    )
    
    clear_button.click(clear_function, None, [chatbot, status_box])
    stats_button.click(stats_function, None, status_box)
    export_button.click(export_function, None, status_box)
    
    # Footer with instructions
    gr.Markdown(
        """
        ---
        ### 📖 How to Use
        
        **Basic Chat:**
        1. Type your message in the text box
        2. Press Enter or click "Send 📤"
        3. The AI will respond with context from previous messages
        
        **Advanced Features:**
        - **System Prompt**: Set a role for the AI (e.g., "You are a Python expert")
        - **Clear Chat**: Reset the conversation and start fresh
        - **Statistics**: View message count and session info
        - **Export**: Save your conversation as JSON
        
        ### 💡 Example Queries
        - "Explain machine learning in simple terms"
        - "Write a Python function to calculate fibonacci numbers"
        - "What's the difference between lists and tuples?"
        - "Help me debug this code: [paste code]"
        
        ### 🔧 Requirements
        - ✅ Ollama must be running: `ollama serve`
        - ✅ Model must be downloaded: `ollama pull llama2`
        - ✅ Check available models: `ollama list`
        
        ### 🚨 Troubleshooting
        If you see errors:
        1. Check Ollama is running: `ps aux | grep ollama`
        2. Test Ollama directly: `ollama run llama2 "hello"`
        3. Check Ollama status: `curl http://localhost:11434`
        """
    )

# Launch the app
if __name__ == "__main__":
    print("="*80)
    print("🚀 AI Agent Proxy Interface Starting...")
    print("="*80)
    print(f"📦 Model: {agent.model_name}")
    print(f"🌡️  Temperature: {agent.temperature}")
    print(f"🔗 Using: Ollama + Gradio")
    print("="*80)
    print("\n⚠️  Make sure Ollama is running:")
    print("   Terminal 1: ollama serve")
    print(f"   Terminal 2: ollama pull {agent.model_name}")
    print("="*80)
    print("\n🌐 Starting web interface...\n")
    
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True,
        quiet=False
    )