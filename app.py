import streamlit as st
from mission_control.ingest import add_pdf, add_url
from mission_control.agent import mission_query

st.title("🚀 Mission Control AI")
st.subheader("Agentic RAG for Mission-Critical Decision Making")

query = st.text_input("Enter your question:")
risk_mode = st.checkbox("Enable Risk Analysis Mode")

if st.button("Run Query") and query:
    with st.spinner("Processing..."):
        response = mission_query(query, risk_analysis=risk_mode)
        st.markdown(response)

st.markdown("---")
st.subheader("📄 Add to Knowledge Base")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
if uploaded_file:
    with open(f"data/docs/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.read())
    add_pdf(f"data/docs/{uploaded_file.name}")
    st.success("PDF added to knowledge base!")

url_input = st.text_input("Add URL")
if st.button("Add URL") and url_input:
    add_url(url_input)
    st.success("URL added to knowledge base!")
