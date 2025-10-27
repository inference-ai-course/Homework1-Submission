import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from part2.main import get_completion


text = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. It has applications in various fields, including healthcare, finance, and transportation.
"""

messages=[{"role": "user", "content":f"Summarize the following text:\n{text}" }] 
response = get_completion(messages)
print(response)
