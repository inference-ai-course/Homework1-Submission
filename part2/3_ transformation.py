import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from part2.main import get_completion


text = "The weather is nice today."

messages=[{"role": "user", "content":f"Translate the following text to French:\n{text}" }]
response = get_completion(messages)
print(response)