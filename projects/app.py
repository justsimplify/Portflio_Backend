from flask import Flask, jsonify
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
DJANGO_PARAM = "Django"
RABBIT_MQ_PARAM = "RabbitMQ"
FLASK_PARAM = "Flask"
VUE_PARAM = "Vue JS"
MONGO_PARAM = "Mongo DB"
JAVA_PARAM = "Java"

PHYSIOHEALS_DESC = "Worked on building a forum where people can ask questions and authorized people could answer the same.\nWorked on creating a blogging system where authorized admins could post and manage blogs.\nWorked on file management where admins could upload files such as videos, ppt etc.\nWorked on a Linking system as well where admins could post links and categorize links as well and manage them as well."
SERVER_MANAGER_DESC = "Worked on the tool where people could manage files, create folders and manage them.\nUI was built to download, upload and read data (supported types only)."
HOME_AUTOMATION_DESC = "Worked on the System to fetch state of the system i.e. on or off using the Python program.\nMade an automation tool which could control devices in the home."
STATUS_CHECKER_DESC = "Developed the tool which can check the service status based on URL.\nBased on the message dispatcher model which will continuously send the status of service to hook.\nHook updates the database which in-turn updates the dashboard."
NODE_HEALTH_CHECK_DESC = "Developed the simplified tool which does the handshakes to GCP Cluster on certain ports based on product specified and returns if the node port is healthy."
PROVISION_DESC = "Developed a provisioner tool for Databases.\nThe user raises the specification request and Jenkins pipeline provisions the database based on that specification by running the application."
SERVICE_VIRTUAL_DESC = "Designed the Python Layer to interact with Java layer on the backend.\nThe layer used to perform operations on Docker runtime and automation on other operations.\nWorked on Customization on Wiremock (open-source tool) to cater to our requirements."

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
    projectDetails.append(createDetails("Status Checker", STATUS_CHECKER_DESC, [
                          DJANGO_PARAM, PYTHON_PARAM, RABBIT_MQ_PARAM, MONGO_PARAM]))
    projectDetails.append(createDetails(
        "Node Health Checker", NODE_HEALTH_CHECK_DESC, [PYTHON_PARAM, FLASK_PARAM]))
    projectDetails.append(createDetails(
        "Provisioning tool", PROVISION_DESC, [PYTHON_PARAM, FLASK_PARAM]))
    projectDetails.append(createDetails("Service Virtualization Tool", SERVICE_VIRTUAL_DESC, [
                          VUE_PARAM, PYTHON_PARAM, FLASK_PARAM, JAVA_PARAM]))
    projectDetails.append(createDetails("Physioheals", PHYSIOHEALS_DESC, [
                          EXPRESS_PARAM, FIREBASE_PARAM, ANGULAR_PARAM]))
    projectDetails.append(createDetails("Server Manager", SERVER_MANAGER_DESC, [
                          NODE_PARAM, ANGULAR_PARAM, BASH_PARAM]))
    projectDetails.append(createDetails(
        "Home Automation System", HOME_AUTOMATION_DESC, [PYTHON_PARAM]))
    return projectDetails


@app.route('/')
def index():
    return jsonify(getProjectDetails())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
