from flask import Flask
from flask import jsonify
from flask_cors import CORS

NAME_PARAM = "projectName"
TECH_STACK_PARAM = "techStack"
PROJECT_DESCRIPTION_PARAM = "projectDescription"

ANGULAR_PARAM = "Angular"
FIREBASE_PARAM = "Firebase"
EXPRESS_PARAM = "Express JS"
MYSQL_PARAM = "MySQL"
BASH_PARAM = "Bash"
NODE_PARAM = "Node JS"
PYTHON_PARAM = "Python"
CPP_PARAM = "C++"

PHYSIOHEALS_DESC = "Physiotherapy relevant blog platform where people could also ask Questions in forum."
COMPLAINT_SYSTEM_DESC = "System to manage complaints for the college."
SERVER_MANAGER_DESC = "Locally centralized server to manage files and folders."
HOME_AUTOMATION_DESC = "Worked on script to fetch and store the state of Bot and control it."
LIBRARY_MANAGEMENT_DESC = "System to manage library books information."

app = Flask(__name__)
CORS(app)

def createDetails(name, description, stack):
    details = dict()
    details[NAME_PARAM] = name
    details[PROJECT_DESCRIPTION_PARAM] = description
    details[TECH_STACK_PARAM] = stack
    return details

def getProjectDetails():
    projectDetails = []
    projectDetails.append(createDetails("Physioheals", PHYSIOHEALS_DESC, [EXPRESS_PARAM, FIREBASE_PARAM, ANGULAR_PARAM]))
    projectDetails.append(createDetails("Complaint System", COMPLAINT_SYSTEM_DESC, [ANGULAR_PARAM, EXPRESS_PARAM, MYSQL_PARAM]))
    projectDetails.append(createDetails("Server Manager", SERVER_MANAGER_DESC, [NODE_PARAM, ANGULAR_PARAM, BASH_PARAM]))
    projectDetails.append(createDetails("Home Automation System", HOME_AUTOMATION_DESC, [PYTHON_PARAM]))
    projectDetails.append(createDetails("Library Management System", LIBRARY_MANAGEMENT_DESC, [CPP_PARAM]))
    return projectDetails

@app.route('/')
def index():
    return jsonify(getProjectDetails())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')