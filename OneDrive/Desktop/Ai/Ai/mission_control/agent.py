from mission_control.utils import OPENAI_API_KEY
import openai
import lancedb
from mission_control.risk_analysis import analyze_risk

openai.api_key = OPENAI_API_KEY
DB_PATH = "data/vectordb"

def mission_query(query, risk_analysis=False):
    db = lancedb.connect(DB_PATH)
    table = db.open_table("docs")

    results = table.search(query).limit(5).to_list()
    context = "\n\n".join([r["text"] for r in results])

    completion = openai.ChatCompletion.create(
        model="gpt-5",  # Replace with gpt-4o if no GPT-5 access
        messages=[
            {"role": "system", "content": "You are Mission Control AI, a decision support assistant."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{query}"}
        ],
        temperature=0.2,
        stream=False
    )

    answer = completion.choices[0].message["content"]

    if risk_analysis:
        risk_report = analyze_risk(answer)
        return f"{answer}\n\n---\n{risk_report}"

    return answer
