import lancedb
from mission_control.utils import OPENAI_API_KEY
import fitz  # PyMuPDF
import requests
from bs4 import BeautifulSoup
import os

DB_PATH = "data/vectordb"
os.makedirs("data/docs", exist_ok=True)
os.makedirs(DB_PATH, exist_ok=True)

def get_db():
    return lancedb.connect(DB_PATH)

def add_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    store_text(text, source=file_path)

def add_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n")
    store_text(text, source=url)

def store_text(text, source):
    db = get_db()
    if "docs" not in db.table_names():
        db.create_table("docs", data=[{"text": text, "source": source}])
    else:
        table = db.open_table("docs")
        table.add([{"text": text, "source": source}])
    print(f"Added document from {source}")
