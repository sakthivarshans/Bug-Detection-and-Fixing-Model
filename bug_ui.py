# bug_ui.py

import torch
import gradio as gr
import re
from collections import defaultdict, OrderedDict
from load_qwen_model import load_qwen_model

# Load model
model, tokenizer, device = load_qwen_model()

# LRU Cache
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

# Error Detection
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

# Debugging function
def debug_code(input_code):
    cached = cache.get(input_code)
    if cached:
        return cached

    prompt = f"<|im_start|>system\nYou are an AI code bug detector.\n<|im_end|>\n" \
             f"<|im_start|>user\n{input_code}\n<|im_end|>\n<|im_start|>assistant\n"

    inputs = tokenizer([prompt], return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=512)

    result = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    errors = detect_errors(result)
    cache.put(input_code, (result, errors))
    return result, errors

# Gradio UI
def run_gradio():
    with gr.Blocks() as demo:
        gr.Markdown("#  Bug Detection & Fixing with Qwen2.5\nPaste your Python code to find and fix bugs!")

        code_input = gr.Code(label="🔧 Enter your Python Code", language="python", lines=10)
        debug_btn = gr.Button("🧠 Debug Code")
        output_box = gr.Textbox(label="🔍 Debugging Output", lines=15)
        error_box = gr.Textbox(label="⚠️ Detected Errors", lines=8)

        def process_code(input_code):
            result, error_data = debug_code(input_code)
            error_summary = "\n".join([f"{k}: {v}" for k, v in error_data.items()]) or "No obvious errors detected."
            return result, error_summary

        debug_btn.click(fn=process_code, inputs=code_input, outputs=[output_box, error_box])

    demo.launch(share=True)

if __name__ == "__main__":
    run_gradio()
