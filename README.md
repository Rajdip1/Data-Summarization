# Data Summarization

Short, simple Flask app that summarizes text using a Hugging Face model.

Setup
- Create and activate a Python virtual environment (optional but recommended).
- Install dependencies:

```
pip install -r requirements.txt
```

- Create a `.env` file at the project root with your Hugging Face token:

```
HuggingFace_Token=your_token_here
```

Run

```
python app.py
```

Open the app at `http://127.0.0.1:5000` and paste text to summarize.

Notes
- `app.py` uses the `facebook/bart-large-cnn` model via the Hugging Face inference API.
- Keep your Hugging Face token private and do not commit it to version control.
