from flask import Flask, render_template, request
from transformers import pipeline
import fitz  # PyMuPDF
import os

app = Flask(__name__)
summarizer = pipeline("summarization")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    uploaded_file = request.files['file']
    if uploaded_file.filename.endswith('.pdf'):
        file_path = os.path.join("uploads", uploaded_file.filename)
        uploaded_file.save(file_path)
        text = extract_text_from_pdf(file_path)
    else:
        text = uploaded_file.read().decode('utf-8')

    if len(text) > 1000:
        text = text[:1000]

    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return render_template('index.html', original=text, summary=summary[0]['summary_text'])

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
