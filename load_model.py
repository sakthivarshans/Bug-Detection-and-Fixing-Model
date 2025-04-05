import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_qwen_model():
    model_name = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
    
    # Choose device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Disable sliding window attention warning
    torch.backends.cuda.enable_flash_sdp(True)
    torch.backends.cuda.enable_math_sdp(False)
    torch.backends.cuda.enable_mem_efficient_sdp(True)

    # Load the model
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        trust_remote_code=True,
        device_map="auto"
    )

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True
    )

    return model, tokenizer, device
