import streamlit as st
import ollama
import os
import requests
from bs4 import BeautifulSoup
import math

sq_version = "1.0.1"

model = 'llama3'
tag = 'latest'
token_limit = 200

os.system(f'ollama pull {model}:{tag}')

def summarize_article(url, word_limit):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_html_content = soup.get_text()

    stream = ollama.chat(
        model=f'{model}:{tag}',
        messages=[
            {
                'role': 'user',
                "content": f"""You are a helpful AI that summarizes articles and webpages. 
                You are currently set to function as an 'Instruct' type model, meaning that 
                you will return the summary without any further prompts. 
                Current settings:
                Word Limit: {word_limit}

                The content you will be provided with is in plain text format, extracted 
                from HTML. Summarize the article below, without adding any comments or 
                interpretation. The summary should be ideally {math.floor(word_limit / 100)} 
                to {math.ceil(word_limit / 100)} paragraphs. Here is the content:

                {article_html_content}
                """
            },
        ],
        stream=True,
    )

    summary_placeholder = st.empty()
    summary = ""

    for chunk in stream:
        message_content = chunk.get('message', {}).get('content')
        if message_content:
            summary += message_content
            summary_placeholder.text(summary)

with st.form("summary_form"):
   st.title("SumQuick: Quick Summaries Done Locally")
   url = st.text_input("URL (must include http:// or https://)", key='url')
   word_limit = st.slider("Token Limit (a token is usually around 3/4 of a word):", min_value=100, max_value=500, 
                          value=200, step=50)
   submitted = st.form_submit_button('Summarize!')
   if submitted:
       summarize_article(url, word_limit)

st.markdown(f"""
<footer style='text-align: center; color: grey; position: fixed;'>
    <p style='margin: 20px; padding: 10px;'>
        SumQuick {sq_version} — AI can make mistakes. Check important info.
    </p>
</footer>
""", unsafe_allow_html=True)
