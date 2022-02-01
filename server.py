#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from lib2to3.pgen2 import token
import logging
from asyncio.windows_events import NULL
from http.server import BaseHTTPRequestHandler, HTTPServer

import openai

from tokenizer import TokenizerHelper

class S(BaseHTTPRequestHandler):
    global TokenResult, MaxTokens, MaxRequest
    TokenResult = 800
    MaxTokens = 2049
    MaxRequest = MaxTokens - TokenResult

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_response()
            with open("pages/index.html", 'rb') as f:
                self.wfile.write(f.read())
        else:
            logging.info("GET \nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
            self._set_response()
            self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        if self.path == '/summary':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            # logging.info("POST \nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))
            # logging.info("POST Body:\n%s\n", post_data.decode('utf-8'))

            openai.api_key = "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"
            try:
                # divide el documento en partes para enviarlos a resumir
                th = TokenizerHelper()
                batch = post_data.decode("utf-8")
                lines = batch.splitlines()
                countTokens = 0
                texto = ""
                summary = "Resumen:\n\n"
                
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
                    r = openai.Completion.create(engine="text-curie-001", prompt=texto, max_tokens=TokenResult, temperature=0.11)
                    summary += r['choices'][0]['text']

                respuesta = bytes(summary, "utf-8")
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.send_header("Content-Length", str(len(respuesta)))
                self.end_headers()
                self.wfile.write(respuesta)
            except BaseException as err:
                respuesta = bytes(err.user_message, "utf-8")
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.send_header("Content-Length", str(len(respuesta)))
                self.end_headers()
                self.wfile.write(respuesta)


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Iniciando servidor, puerto: %s...', str(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Detenido...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
