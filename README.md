#  Bug Detection and Fixing AI Model

This project is an AI-powered tool for automatically detecting and fixing bugs in code using Qwen2.5-Coder-1.5B-Instruct, a lightweight Large Language Model (LLM) designed for coding tasks. It also features a simple graphical user interface (GUI) that allows users to input buggy code and receive corrected output.




## 🧠 What It Does

- Accepts buggy code as input (Python syntax).
- Uses the Qwen model to understand and detect the bug.
- Fixes it and provides the corrected version of the code.
- Shows the output in a **Graphical User Interface (GUI)** built using **Gradio**.
- The GUI runs on a local server (IP address will be shown) and can be accessed via a web browser or Android app.


## 💻 How It Works (Flow)

1. `load_qwen_model.py` 
   Loads the Qwen2.5 model and tokenizer from Hugging Face.

2. `bug_detector.py`  
   Contains the logic to:
   - Accept input code.
   - Generate a response from the model.
   - Return the corrected code.

3. `ui.py` 
   Launches a GUI using Gradio.  
   - Paste your buggy code.
   - Click “Submit”.
   - View the fixed version below.

---

## 🚀 How to Run the Project (Step-by-Step)

### 🛠️ 1. Clone the Repository
bash
```git clone https://github.com/your-username/Bug-Detection-and-Fixing-Model.git```
```cd Bug-Detection-and-Fixing-Model```

Create a Virtual Environment (Optional but recommended)
```python -m venv .venv```
```.\.venv\Scripts\activate```    # On Windows

Install all Dependencies
```pip install -r requirements.txt```
Make sure you have transformers, torch, gradio, accelerate, and huggingface_hub.

Login into Huggingface
```huggingface-cli login```
Paste your Hugging Face token (can be generated from https://huggingface.co/settings/tokens).
to paste click " Right click " or ctrl + shift + v

Launch the GUI
```python source_code/ui.py```
This will display a local IP address in the terminal like:
Running on http://127.0.0.1:7860
[Note: if it is aking to download and application click on the link and download it then it will redirect to webpage for the UI implementation ]


📋 Tips
If you get an error like ModuleNotFoundError, ensure your paths are correct and Python environment is activated.

If the model doesn't load, check your Hugging Face token or internet connection.

📌 Final Notes
This model uses a 1.5B parameter LLM, so it's lightweight and runs well on most systems with 8GB+ RAM.

The model is not fine-tuned for all languages — it mainly works with Python.

✅ Summary of What to Do
Step	Action
✅	Clone the repo
✅	Install dependencies
✅	Login to Hugging Face
✅	Run the project using python source_code/ui.py
✅	Use the web UI for bug detection & fixing


👨‍💻 Credits
Model: Qwen2.5-Coder-1.5B-Instruct
GUI: Gradio
Developer: Sakthivarshan S



