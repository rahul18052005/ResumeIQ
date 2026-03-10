def match_skills(resume_skills, required_skills):

    matched = []
    missing = []

    for skill in required_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing