from flask import Flask
from flask import jsonify
from flask_cors import CORS

NAME_PARAM = "skillName"
DESCRIPTION_PARAM = "skillSet"

#Skill Names
PROGRAMMING_LANG = "Programming Languages"
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
    skillDetails.append(createDetails(PROGRAMMING_LANG, ['Python', 'Kotlin', 'Java']))
    skillDetails.append(createDetails(FRAMEWORKS, ['Node.js', 'Express JS', 'React JS', 'Angular JS', 'Django', 'Flask']))
    skillDetails.append(createDetails(DB, ['MySQL', 'MongoDB', 'Firebase Database', 'Cassandra']))
    skillDetails.append(createDetails(CLOUD, ['AWS', 'K8s', 'Docker', 'GCP']))
    skillDetails.append(createDetails(TOOLS, ['GIT', 'Terraform', 'Vault', 'Jenkins', 'Spinnaker']))
    skillDetails.append(createDetails(PLATFORM, ['Web', 'Android']))
    skillDetails.append(createDetails(OS, ['Mac', 'Linux']))
    return skillDetails

@app.route('/')
def index():
    return jsonify(getSkillDetails())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')