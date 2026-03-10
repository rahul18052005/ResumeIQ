# ResumeIQ

ResumeIQ is a web application that helps recruiters evaluate candidate resumes using Natural Language Processing (NLP) and Machine Learning techniques.

The system compares a candidate's resume with a job description and calculates a match score based on skills similarity.

---

## Features

- Resume PDF parsing
- Skill extraction from resumes
- Job description skill extraction
- Match score calculation using TF-IDF and cosine similarity
- Matched skills detection
- Missing skills detection
- Interactive web interface

---

## Tech Stack

### Backend
- Python
- Flask
- Flask-CORS
- Scikit-learn
- spaCy
- pdfminer

### Frontend
- HTML
- CSS
- JavaScript

---

## Project Structure
AI-RESUME-SCREENER
│
├── backend
│ ├── app.py
│ ├── resume_parser.py
│ ├── skill_extractor.py
│ ├── skill_matcher.py
│ └── similarity.py
│
├── frontend
│ ├── index.html
│ ├── script.js
│ └── style.css
│
├── resumes
│ └── sample_resume.pdf
│
├── requirements.txt
├── run_project.bat
├── README.md
└── .gitignore


---

## How It Works

1. Recruiter enters the job description.
2. Candidate uploads a resume (PDF format).
3. The system extracts text from the resume.
4. Skills are detected using NLP techniques.
5. TF-IDF and cosine similarity calculate the match score.
6. The dashboard displays detected skills, matched skills, and missing skills.

---

## Run the Project Locally

Install dependencies:
pip install -r requirements.txt


## Run backend server:


python backend/app.py


## Run frontend server:


cd frontend
python -m http.server 5500


## Open in browser:


http://localhost:5500/index.html


---

## Future Improvements

- Multiple resume ranking system
- Advanced NLP skill extraction
- Resume recommendation system
- Cloud deployment