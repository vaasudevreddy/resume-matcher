import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text


# Overall similarity
def calculate_match(resume_text, jd_text):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_clean, jd_clean])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(similarity[0][0] * 100, 2)


# Extract important keywords (skills proxy)
def extract_keywords(text):
    doc = nlp(text.lower())
    return list(set([token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]))


# Skill matching
def skill_analysis(resume_text, jd_text):
    resume_skills = set(extract_keywords(resume_text))
    jd_skills = set(extract_keywords(jd_text))

    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills - resume_skills

    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = round((len(matched) / len(jd_skills)) * 100, 2)

    return skill_score, list(missing)[:10]


# Section scoring
def section_analysis(resume_text, jd_text):

    sections = {
        "skills": "",
        "projects": "",
        "experience": "",
        "summary": ""
    }

    resume_lower = resume_text.lower()

    for key in sections.keys():
        if key in resume_lower:
            sections[key] = resume_lower.split(key)[1]

    section_scores = {}

    for section, content in sections.items():
        if content.strip() != "":
            section_scores[section] = calculate_match(content, jd_text)

    return section_scores