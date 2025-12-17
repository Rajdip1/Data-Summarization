from flask import Flask, render_template, request as req, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])

def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=['GET','POST'])
def Summarize():
    if req.method=='POST':
        API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
        headers = {
        "Authorization": f"Bearer {os.getenv('HuggingFace_Token')}",
        }

        data = req.form["data"]

        maxLength = int(req.form['maxLength'])
        minLength = maxLength//4

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data, 
            "parameters": {"min_length": minLength,"max_length": maxLength,}
        })[0]
        return render_template("index.html", result=output['summary_text'])
    else:
        return render_template("index.html")

if __name__=='__main__':
    app.debug = True
    app.run()