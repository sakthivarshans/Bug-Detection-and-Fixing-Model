# load_qwen_model.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def load_qwen_model():
    model_name = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    )
    
    print("✅ Qwen2.5-Coder-1.5B-Instruct model loaded successfully!")
    return model, tokenizer, device
