import streamlit as st
from utils.parser import extract_text
from utils.skill_extractor import extract_skills
from utils.matcher import match_score
st.title("AI Resume Screening System")
resume=st.file_uploader("Upload Resume",type=["pdf"])
jd=st.text_area("Job Description")
if st.button("Analyze"):
    if resume and jd:
        txt=extract_text(resume)
        st.write("Skills:",extract_skills(txt))
        s=match_score(txt,jd)
        st.progress(int(s)); st.write(f"Score: {s:.1f}%")
