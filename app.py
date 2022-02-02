from lib2to3.pgen2 import token
import logging
from asyncio.windows_events import NULL

import openai

from tokenizer import TokenizerHelper

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

global TokenResult, MaxTokens, MaxRequest
TokenResult = 800
MaxTokens = 2049
MaxRequest = MaxTokens - TokenResult

@app.route('/') 
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/summary', methods=['POST'])
def summary():
    openai.api_key = "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"
    # divide el documento en partes para enviarlos a resumir
    th = TokenizerHelper()
    message = request.data
    batch = message.decode("utf-8")
    lines = batch.splitlines()
    countTokens = 0
    texto = ""
    summary = "Resumen:\n\n"
        
    try:
        for line in lines:
            if len(line) == 0: continue
            tokens = th.CountTokens(line)
            if (countTokens + tokens) < MaxRequest or tokens == 0:
                texto += line + "\n"
                countTokens += tokens
            else:
                texto += "\n\nTl;dr:"
                logging.info("Count Tokens:%s", str(countTokens))
                r = openai.Completion.create(engine="text-curie-001", prompt=texto, max_tokens=TokenResult, temperature=0.11)
                summary += r['choices'][0]['text']
                texto = line + "\n"
                countTokens = tokens
        
        # queda una ultima linea
        if len(texto.strip()) > 0:
            texto += "\n\nTl;dr:"
            r = openai.Completion.create(engine="text-curie-001", prompt=texto, max_tokens=TokenResult, temperature=0.11)
            summary += r['choices'][0]['text']

        respuesta = bytes(summary, "utf-8")
        return respuesta
    except BaseException as err:
        respuesta = bytes(err.user_message, "utf-8")
        return respuesta


if __name__ == '__main__':
   app.run()