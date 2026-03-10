from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from skill_matcher import match_skills

resume = extract_resume_text("resumes/sample_resume.pdf")

resume_skills = extract_skills(resume)

required_skills = [
    "python",
    "machine learning",
    "sql",
    "docker"
]

matched, missing = match_skills(resume_skills, required_skills)

print("Detected Skills:", resume_skills)
print("Matched Skills:", matched)
print("Missing Skills:", missing)