from resume_parser import extract_resume_text
from skill_extractor import extract_skills

resume = extract_resume_text("resumes/sample_resume.pdf")

skills = extract_skills(resume)

print("Detected Skills:")
print(skills)