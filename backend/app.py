from flask import Flask, request, jsonify
from flask_cors import CORS

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from skill_matcher import match_skills
from similarity import calculate_similarity



app = Flask(__name__)
CORS(app)


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    job_description = request.form["job_description"]
    resume_file = request.files["resume"]

    file_path = "temp_resume.pdf"
    resume_file.save(file_path)

    resume_text = extract_resume_text(file_path)

    resume_skills = extract_skills(resume_text)

    required_skills = extract_skills(job_description)

    matched, missing = match_skills(resume_skills, required_skills)

    score = calculate_similarity(resume_text, job_description)

    result = {
        "match_score": score,
        "resume_skills": resume_skills,
        "matched_skills": matched,
        "missing_skills": missing
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)