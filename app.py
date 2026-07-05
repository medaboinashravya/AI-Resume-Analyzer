import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Welcome! Upload your resume to analyze your skills.")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Resume Text")
    st.write(text)
