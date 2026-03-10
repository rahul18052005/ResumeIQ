from resume_parser import extract_resume_text
from similarity import calculate_similarity

resume = extract_resume_text("resumes/sample_resume.pdf")

job_description = """
Looking for a software engineer with skills in Python,
machine learning and SQL.
"""

score = calculate_similarity(resume, job_description)

print("Resume Match Score:", score)