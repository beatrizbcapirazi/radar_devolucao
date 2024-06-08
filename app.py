from flask import Flask, render_template, request
import requests as rq
from bs4 import BeautifulSoup as bs
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(port=5000, debug=True)
