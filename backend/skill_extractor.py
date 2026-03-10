skills = [
    "python",
    "machine learning",
    "sql",
    "data analysis",
    "deep learning",
    "java",
    "c++",
    "html",
    "css",
    "javascript",
    "tensorflow",
    "pandas",
    "numpy",
]
def extract_skills(resume_text):

    resume_text = resume_text.lower()

    found_skills = []

    for skill in skills:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills