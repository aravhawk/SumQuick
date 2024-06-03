# SumQuick

#### A GPU is highly recommended for running SumQuick (or any Ollama/AI model), otherwise inference may take quite a while. Compatible GPUs listed at https://github.com/ollama/ollama/blob/main/docs/gpu.md

## About
An open-source AI summarization tool that runs locally, using Ollama!

## Features
- Local execution for privacy and security
- Summarizes text efficiently using AI
- User-friendly interface with Streamlit

## Installation

### Prerequisites
- Python 3.11
- Pip (Python package installer)
- Ollama (visit https://ollama.com/download if not already installed)

### Clone the Repository
```zsh
git clone https://github.com/aravhawk/SumQuick.git
cd SumQuick
pip3 install -r requirements.txt
streamlit run main.py
```

### Use the App

#### On the host computer
- Visit localhost:8501 or 127.0.0.1:8501 in a web browser

#### On another device within the network
- Visit <host-computer-ip>:8501 in a web browser

## Tweaks & Using Other Models

- To use (or experiment with) other Ollama-compatible models in SumQuick, simply edit lines 8 and 9 in main.py, with your model choice and one of its corresponding tags.
- For example:
```python
model = 'llama3'
tag = 'latest'
```
or
```python
model = 'llama3'
tag = '8b-instruct-q8_0'
```
A full catalog of all models, tags, etc. is available at https://ollama.com/library.
