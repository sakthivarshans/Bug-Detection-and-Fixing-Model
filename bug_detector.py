import torch
import re
from collections import defaultdict, OrderedDict
from load_qwen_model import load_qwen_model

# Load Qwen model, tokenizer, and device
model, tokenizer, device = load_qwen_model()

# LRU Cache to avoid repeated computation
class LRUCache:
    def __init__(self, capacity=10):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

# Initialize cache
cache = LRUCache()

# Error detection patterns
def detect_errors(debug_output):
    patterns = {
        "Syntax Error": r"SyntaxError",
        "Type Error": r"TypeError",
        "Name Error": r"NameError",
        "Index Error": r"IndexError",
        "Key Error": r"KeyError",
        "Attribute Error": r"AttributeError",
        "Value Error": r"ValueError",
        "Indentation Error": r"IndentationError",
        "Import Error": r"ImportError",
        "ZeroDivision Error": r"ZeroDivisionError"
    }
    error_counts = defaultdict(int)
    for err_type, pattern in patterns.items():
        error_counts[err_type] += len(re.findall(pattern, debug_output))
    return dict(error_counts)

# Main function to debug code
def debug_code(input_text):
    cached = cache.get(input_text)
    if cached:
        return cached

    # Prepare prompt
    prompt = (
        "<|im_start|>system\nYou are an AI code bug detector.\n<|im_end|>\n"
        f"<|im_start|>user\n{input_text}\n<|im_end|>\n<|im_start|>assistant\n"
    )

    inputs = tokenizer([prompt], return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=512)

    # Decode only the newly generated text
    result = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)

    # Detect and count errors
    errors = detect_errors(result)

    # Save to cache
    cache.put(input_text, (result, errors))

    return result, errors
