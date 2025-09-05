# 🚀 LinkedIn Post Generator (Free AI Demo)

A local AI tool that generates professional LinkedIn posts based on a topic and language selection (English, Bengali, Spanish).  

## Features
- Generates 3–4 paragraph LinkedIn-style posts.
- Download posts as `.txt`.
- Runs entirely locally using the GPT4All LORA model.

## Requirements
- Python 3.10+
- Streamlit, Transformers, Torch, SentencePiece
- Install dependencies: `pip install -r requirements.txt`

## Usage
Run the app:
```bash
streamlit run app.py
```

...

## Notes

- The GPT model `gpt4all-lora-quantized.bin` is **not included** in this repository due to size limitations. You can download it from [Google Drive](https://drive.google.com/drive/folders/1HNQ1rldmtHPT23un8zPtYLfkv7k38f9w?usp=sharing) and place it in the project root directory.  
- The demo video is also **hosted externally** because it exceeds GitHub's file size limit. You can view/download it from [Google Drive link](https://drive.google.com/drive/folders/1HNQ1rldmtHPT23un8zPtYLfkv7k38f9w?usp=sharing).  
- Make sure to install all dependencies from `requirements.txt` before running the app.  
- The app runs locally; no internet connection is required for generating posts once the model is downloaded.
- So, for `gpt4all-lora-quantized.bin` and `requirements.txt`, [click this google drive link](https://drive.google.com/drive/folders/1HNQ1rldmtHPT23un8zPtYLfkv7k38f9w?usp=sharing)
