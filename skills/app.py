from flask import Flask
from flask import jsonify
from flask_cors import CORS

NAME_PARAM = "skillName"
DESCRIPTION_PARAM = "skillSet"

#Skill Names
PROGRAMMING_LANG = "Programming Languages"
WEB_TECH = "Web Technologies"
FRAMEWORKS = "Frameworks / APIs"
DB = "Database"
CLOUD = "Cloud Services / Tools"
TOOLS = "Tools"
PLATFORM = "Platforms"
OS = "Operating System"

app = Flask(__name__)
CORS(app)

def createDetails(name, skillSet):
    details = dict()
    details[NAME_PARAM] = name
    details[DESCRIPTION_PARAM] = skillSet
    return details

def getSkillDetails():
    skillDetails = []
    skillDetails.append(createDetails(PROGRAMMING_LANG, ['Python', 'C/C++', 'Bash', 'Java', 'Kotlin']))
    skillDetails.append(createDetails(WEB_TECH, ['HTML', 'CSS', 'JavaScript', 'TypeScript']))
    skillDetails.append(createDetails(FRAMEWORKS, ['MEAN', 'Django', 'Firebase', 'AWS Lex', 'Lambdas', 'Google Assistant', 'Maps and Places', 'Vue JS']))
    skillDetails.append(createDetails(DB, ['MySQL', 'MongoDB', 'Firebase Database']))
    skillDetails.append(createDetails(CLOUD, ['AWS', 'Docker', 'Kubernetes (Basic)', 'VMWare (Basic)']))
    skillDetails.append(createDetails(TOOLS, ['ServiceNow (ITSM)', 'PagerDuty', 'Jenkins', 'Git']))
    skillDetails.append(createDetails(PLATFORM, ['Web', 'Android']))
    skillDetails.append(createDetails(OS, ['Mac', 'Linux']))
    return skillDetails

@app.route('/')
def index():
    return jsonify(getSkillDetails())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')