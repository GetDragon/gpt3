#from lib2to3.pgen2 import token
#from datetime import datetime

from summary import SpacyHelper
from summaryoai import OpenAIHelper
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/') 
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/summary2', methods=['POST'])
def summarySpacy():
    ss = SpacyHelper()
    return ss.summarize(request.data.decode("utf-8"), 0.2)

@app.route('/summary', methods=['POST'])
def summary():
    oaih = OpenAIHelper()
    batch = request.data.decode("utf-8")
    return oaih.summaryAI(batch)

if __name__ == '__main__':
   app.run()