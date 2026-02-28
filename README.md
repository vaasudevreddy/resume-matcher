# AI Resume Ranking System 🚀

An intelligent ATS-style Resume Ranking System that evaluates multiple resumes against a job description and ranks them based on similarity score, skill match percentage, and section-wise analysis.

This project simulates how Applicant Tracking Systems (ATS) filter and rank resumes using Natural Language Processing (NLP).

------------------------------------------------------------

🔥 FEATURES

- Upload multiple resumes (.pdf, .docx, .txt)
- Paste job description
- Overall similarity score (TF-IDF + Cosine Similarity)
- Skill match percentage
- Missing skill detection
- Section-wise analysis (Skills, Projects, Experience, Summary)
- Resume ranking (highest match first)
- Modern UI
- Deployable to cloud (Render)

------------------------------------------------------------

🧠 TECH STACK

Backend:
- Python
- Flask

NLP & ML:
- Scikit-learn (TF-IDF, Cosine Similarity)
- spaCy (Keyword & Skill Extraction)

File Processing:
- PDFPlumber
- python-docx

Deployment:
- Gunicorn
- Render

Frontend:
- HTML
- CSS

------------------------------------------------------------

⚙️ LOCAL INSTALLATION

1. Clone repository:

git clone https://github.com/vaasudevreddy/resume-matcher.git
cd resume-matcher

2. Create virtual environment:

python3.11 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Download spaCy model:

python -m spacy download en_core_web_sm

5. Run application:

python app.py

Open browser:

http://127.0.0.1:5000

------------------------------------------------------------

🌍 DEPLOYMENT (Render)

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app

------------------------------------------------------------

📊 HOW IT WORKS

1. Extract text from uploaded resumes.
2. Clean and preprocess text.
3. Convert resume and job description into TF-IDF vectors.
4. Compute cosine similarity score.
5. Extract important keywords using spaCy.
6. Calculate skill match percentage.
7. Analyze resume sections individually.
8. Rank resumes based on overall score.

------------------------------------------------------------

🎯 FUTURE IMPROVEMENTS

- Replace TF-IDF with BERT embeddings
- Add database to store results
- User authentication system
- Resume improvement suggestions
- Recruiter dashboard UI
- Skill ontology-based intelligent matching
- Score explanation engine
- File size validation and security enhancements

------------------------------------------------------------

👨‍💻 AUTHOR

Vaasu Reddy
AI Enthusiast