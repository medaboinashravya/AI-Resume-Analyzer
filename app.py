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
    skills = [
    "Python", "Java", "C", "C++", "SQL",
    "HTML", "CSS", "JavaScript",
    "Machine Learning", "Git", "GitHub",
    "Excel", "Streamlit"
]

found_skills = []

for skill in skills:
    if skill.lower() in text.lower():
        found_skills.append(skill)


st.subheader("Skills Found")

if found_skills:
    for skill in found_skills:
        st.write("✅", skill)
else:
    st.write("No matching skills found.")
    st.subheader("ATS Score")

total_skills = len(skills)
score = (len(found_skills) / total_skills) * 100

st.progress(int(score))
st.write(f"Your ATS Score: {score:.0f}/100")
missing_skills = []

for skill in skills:
    if skill not in found_skills:
        missing_skills.append(skill)

st.subheader("Skills to Learn")

if missing_skills:
    for skill in missing_skills:
        st.write("❌", skill)
else:
    st.write("Excellent! No missing skills.")
