import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from part2.main import get_completion


text = """
John Doe, a 29-year-old software engineer from San Francisco, recently joined OpenAI as a research scientist.
"""
messages=[{"role": "user", "content":f"Extract the name and occupation from the following text:\n{text}" }]

print(get_completion(messages))