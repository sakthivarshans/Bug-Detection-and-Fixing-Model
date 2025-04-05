# ------------------------ load_qwen_model.py ------------------------
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"

def load_qwen_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    print("\n✅ Qwen2.5-Coder-1.5B-Instruct model loaded successfully!")
    return model, tokenizer, device

# ------------------------ bug_detector.py ------------------------
import torch
from collections import OrderedDict
from load_qwen_model import load_qwen_model

model, tokenizer, device = load_qwen_model()

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

cache = LRUCache()

def debug_code(input_text):
    cached = cache.get(input_text)
    if cached:
        return cached

    prompt = f"<|im_start|>system\nYou are an AI code bug detector.\n<|im_end|>\n" \
             f"<|im_start|>user\n{input_text}\n<|im_end|>\n<|im_start|>assistant\n"

    inputs = tokenizer([prompt], return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=512)

    result = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    cache.put(input_text, result)
    return result

# ------------------------ ui.py ------------------------
import gradio as gr
from bug_detector import debug_code

def process_code(input_code):
    debug_output = debug_code(input_code)
    return debug_output

with gr.Blocks() as demo:
    gr.Markdown("""
    # 🐞 AI Bug Detection and Fixing
    Paste your Python code below and let the AI assist you in finding and fixing issues.
    """)

    with gr.Row():
        code_input = gr.Code(label="Enter Python Code", language="python")
        debug_button = gr.Button("🔍 Analyze Code")

    output_box = gr.Textbox(label="AI Debugging Output", lines=20)

    debug_button.click(fn=process_code, inputs=code_input, outputs=output_box)

if __name__ == "__main__":
    demo.launch(share=True)
