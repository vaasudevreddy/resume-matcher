from flask import Flask, render_template, request
import pdfplumber
import docx
from matcher import calculate_match, skill_analysis, section_analysis

app = Flask(__name__)



def extract_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception:
        return ""
    return text


def extract_docx(file):
    try:
        doc = docx.Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception:
        return ""


def extract_txt(file):
    try:
        return file.read().decode("utf-8")
    except Exception:
        return ""


def extract_text(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return extract_pdf(file)
    elif filename.endswith(".docx"):
        return extract_docx(file)
    elif filename.endswith(".txt"):
        return extract_txt(file)
    else:
        return ""



@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        resume_files = request.files.getlist("resume")
        jd_text = request.form.get("jd", "")

        if not resume_files or jd_text.strip() == "":
            return "Please upload resumes and provide a job description."

        results = []

        for file in resume_files:

            resume_text = extract_text(file)

            if resume_text.strip() == "":
                continue

        
            overall_score = calculate_match(resume_text, jd_text)

         
            skill_score, missing_skills = skill_analysis(resume_text, jd_text)

            
            sections = section_analysis(resume_text, jd_text)

            results.append({
                "name": file.filename,
                "score": overall_score,
                "skill_score": skill_score,
                "missing": missing_skills,
                "sections": sections
            })


        results = sorted(results, key=lambda x: x["score"], reverse=True)

        return render_template("ranking.html", results=results)

    return render_template("index.html")
