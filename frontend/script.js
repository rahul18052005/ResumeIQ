async function analyzeResume(){

let jd = document.getElementById("job_description").value
let resume = document.getElementById("resume").files[0]

let formData = new FormData()

formData.append("job_description", jd)
formData.append("resume", resume)

let response = await fetch("http://127.0.0.1:5000/analyze",{
method:"POST",
body:formData
})

let data = await response.json()

let score = (data.match_score * 100).toFixed(1)

let progress = document.getElementById("progress")

progress.style.width = score + "%"
progress.innerText = score + "%"

showSkills("resume-skills",data.resume_skills)
showSkills("matched-skills",data.matched_skills)
showSkills("missing-skills",data.missing_skills)

}

function showSkills(id,skills){

let container = document.getElementById(id)

container.innerHTML=""

skills.forEach(skill=>{

let tag = document.createElement("span")

tag.className="bg-gray-200 px-3 py-1 rounded-full text-sm"

tag.innerText = skill

container.appendChild(tag)

})

}