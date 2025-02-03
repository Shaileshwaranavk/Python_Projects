import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the NLP model
nlp = spacy.load('en_core_web_sm')

# Sample function to remove text from a PDF file
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""  # Append the text from each page
    return text

# Sample data: PDF file paths for resumes
resume_paths = [
    "resume1.pdf",
    "resume2.pdf",
]

# Sample job description
job_description = """
Seeking a Python developer with experience in Django, Flask, and SQL. Knowledge of machine learning is a plus.
"""

# Step 1: Preprocessing function
def preprocess_text(text):
    text = text.lower().strip()
    return text

# Step 2: Remove skills and experience
def extract_skills_and_experience(text):
    doc = nlp(text)
    skills = []
    # Sample list of known skills
    known_skills = ["python", "django", "flask", "sql", "machine learning", "html", "css", "javascript", "react", "tableau", "power bi", "data visualization"]

    # Remove skills based on known skills
    for token in doc:
        if token.text.lower() in known_skills:
            skills.append(token.text.lower())

    # Remove experience phrases
    experience = []
    for sent in doc.sents:
        if "years" in sent.text or "experience" in sent.text:
            experience.append(sent.text.strip())

    return set(skills), experience

# The Process resumes to remove skills and experience
resume_data = []
for path in resume_paths:
    text = extract_text_from_pdf(path)
    preprocessed_text = preprocess_text(text)
    skills, experience = extract_skills_and_experience(preprocessed_text)
    resume_data.append({"skills": skills, "experience": experience, "processed_text": preprocessed_text})

# Process the job description
preprocessed_job_description = preprocess_text(job_description)
job_skills, job_experience = extract_skills_and_experience(preprocessed_job_description)

# Step 3: Feature extraction with TF-IDF
vectorizer = TfidfVectorizer()
documents = [data["processed_text"] for data in resume_data] + [preprocessed_job_description]
tfidf_matrix = vectorizer.fit_transform(documents)

# Step 4: Calculate similarity scores
job_vector = tfidf_matrix[-1]  # Job description vector
resume_vectors = tfidf_matrix[:-1]  # Resume vectors
scores = cosine_similarity(resume_vectors, job_vector)

# Step 5: Rank candidates
candidate_scores = [(i + 1, score[0], resume_data[i]["skills"], resume_data[i]["experience"]) for i, score in enumerate(scores)]
ranked_candidates = sorted(candidate_scores, key=lambda x: x[1], reverse=True)

# Step 6: Output results
print("Ranking of Candidates based on Job Description Match:")
for rank, (candidate_id, score, skills, experience) in enumerate(ranked_candidates, 1):
    print(f"Rank {rank}: Candidate {candidate_id} with Score {score:.2f}")
    print(f"  Extracted Skills: {', '.join(skills)}")
    print(f"  Information: {', '.join(experience)}")
