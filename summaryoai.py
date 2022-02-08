import os
import openai
import logging
from tokenizer import TokenizerHelper

class OpenAIHelper:
    global TokenResult, MaxTokens, MaxRequest
    
    
    def __init__(self):
        self.TokenResult = 800
        self.MaxTokens = 2049
        self.MaxRequest = self.MaxTokens - self.TokenResult

    def summaryAI(self, data):
        th = TokenizerHelper()
        lines = data.splitlines()
        countTokens = 0
        texto = ""
        summary = ""
        openai.api_key = "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" #os.environ.get("API_KEY")
        try:
            for line in lines:
                if len(line) == 0: continue
                tokens = th.CountTokens(line)
                if (countTokens + tokens) < self.MaxRequest or tokens == 0:
                    texto += line + "\n"
                    countTokens += tokens
                else:
                    texto += "\n\nTl;dr:"
                    logging.info("Count Tokens:%s", str(countTokens))
                    r = openai.Completion.create(engine="text-curie-001", prompt=texto, max_tokens=self.TokenResult, temperature=0.11)
                    summary += r['choices'][0]['text']
                    texto = line + "\n"
                    countTokens = tokens
            
            # queda una ultima linea
            if len(texto.strip()) > 0:
                texto += "\n\nTl;dr:"
                r = openai.Completion.create(engine="text-curie-001", prompt=texto, max_tokens=self.TokenResult, temperature=0.11)
                summary += r['choices'][0]['text']

            respuesta = bytes(summary, "utf-8")
            return respuesta
        except BaseException as err:
            respuesta = bytes(err.user_message, "utf-8")

        return respuesta