# 🚀 Mission Control AI

Mission Control AI is an **Agentic Retrieval-Augmented Generation (RAG)** system designed for **mission-critical decision support**.

It allows you to:
- Ingest **PDFs** and **webpages** into a LanceDB vector store.
- Query them using **OpenAI GPT models**.
- Enable **Risk Analysis Mode** for confidence scoring.

## Features
✅ Document ingestion (PDF & URL)  
✅ Agentic RAG pipeline  
✅ Risk scoring for decision-making  
✅ Streamlit UI for easy use  

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/mission-control-ai.git
cd mission-control-ai
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
```

## Run the App
```bash
streamlit run app.py
```

---
Built by Alexander Dorozynski
