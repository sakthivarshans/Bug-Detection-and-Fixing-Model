🐞 Bug Detection and Fixing AI Model
Welcome to the Bug Detection and Fixing AI project! This project uses a powerful LLM (Qwen2.5-Coder-1.5B) to automatically detect and fix code bugs using artificial intelligence.

Whether you’re a beginner or a developer, this guide will walk you through everything — from setup to launching the app.

# 📌 Project Highlights
✅ Detects syntax, logical, and structural bugs

🛠️ Fixes bugs using trained AI

🧠 Based on Qwen2.5-Coder-1.5B-Instruct

💻 Easy-to-use Graphical Interface (Gradio)

📊 Supports Python source code

🐍 Works offline in VS Code, or you can host it on Hugging Face

# 📂 Project Structure
bash
Copy
Edit
Bug-Detection-and-Fixing-Model/
│
├── load_qwen_model.py      # Loads the Qwen2.5 model
├── bug_detector.py         # Logic to detect and fix bugs
├── app.py                  # Gradio UI (entry point)
├── source_code             # Folder with code examples or dataset
├── requirements.txt        # Python packages required
├── README.md               # This file
└── .venv/ (optional)       # Your virtual environment

 I suggest you to use the source code as second option use the other code like the independent modules and run the model.
 
⚙️ How to Set Up (Run Locally)
1. 📥 Clone the Repository 
```git clone https://github.com/your-username/Bug-Detection-and-Fixing-Model.git``` 
```cd Bug-Detection-and-Fixing-Model``` 
2. 🐍 Create & Activate Virtual Environment 
# Windows
```python -m venv .venv``` 
```.venv\Scripts\activate``` 

# Mac/Linux
```python3 -m venv .venv``` 
```source .venv/bin/activate``` 
3. 📦 Install Requirements 

```pip install -r requirements.txt```

🚀 How to Run the Model
🔹 Step 1: Load the Model 

No need to run this manually — it's done automatically inside app.py using: 

python
```from load_qwen_model import load_qwen_model``` 

This loads the Qwen2.5-Coder model and tokenizer. 

# Load the load_qwen_model.py to install the model in your computer 

🔹 Step 2: Run the Interface 
Use the command below to start the web UI: 

```python app.py``` 
You will see something like: 


```Running on local URL: http://127.0.0.1:7860``` 
 Click the link or open it in your browser. 
 [Note: if it is asking to download and application click on the link and download it then it will redirect to webpage for the UI implementation ]

🧠 How the UI Works 
🖊️ Paste your Python code in the text box. 

🤖 The model will detect bugs and suggest fixes. 

📥 You can copy the fixed code. 

✅ No need to download anything else. It runs in your browser locally. 

# 📌 Tips
If you see ModuleNotFoundError, ensure you're in the .venv and all dependencies are installed. 

Use app.py to launch the project. Other files are used internally. 

and also the main and all the works done in the project is given in the report in the document folder 

# 🧑‍💻 Credits
Model: Qwen2.5-Coder-1.5B-Instruct  
Interface: Gradio  
Developer: Sakthivarshan S


