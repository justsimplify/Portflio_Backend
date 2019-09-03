from flask import Flask, jsonify
from flask_cors import CORS

NAME_PARAM = "companyName"
DESIGNATION_PARAM = "designation"
JOB_DESCRIPTION_PARAM = "description"
LOCATION_PARAM = "location"
FROM_PARAM = "fromDate"
TO_PARAM = "toDate"

app = Flask(__name__)
CORS(app)


def createDetails(name, designation, description, location, fromDate, toDate):
    details = dict()
    details[NAME_PARAM] = name
    details[DESIGNATION_PARAM] = designation
    details[JOB_DESCRIPTION_PARAM] = description
    details[LOCATION_PARAM] = location
    details[FROM_PARAM] = fromDate
    details[TO_PARAM] = toDate
    return details


def lowesJobRole():
    role = []
    role.append("Working on Platform Persistence team to provision DBs for application teams as per their requirements. Also working on automation of multiple tasks such as provisioning instances, VMs etc with required services on GCP.")
    role.append("This enhanced the process of provision of databases rather than doing it manually and reduced the number of errors in the databases.")
    role.append("Worked on Associate Android App for Easing workflow for Lowe’s Store Employees and Consumer App feature improvements.")
    role.append("Worked on Service Virtualization tool based on Wiremock.")
    return role


def appviewxRole():
    role = []
    role.append(
        "Designed several pipelines using Jenkins to automate the process of VM Creation and Volume Mounting.")
    role.append("Deployed Python Scripts for provisioning of containers which optimized the process of automation and reduced time for the same.")
    role.append(
        "Worked on ITSM Tool ServiceNow and Incident Resolution Platform PagerDuty to integrate with the Product.")
    return role


def getExperienceDetails():
    experienceDetails = []
    experienceDetails.append(createDetails("Lowe's India", "Software Engineer", lowesJobRole(
    ), "Bangalore, India", "August 2017", "Present"))
    experienceDetails.append(createDetails("AppViewX / Payoda", "DevOps Engineering Intern",
                                           appviewxRole(), "Coimbatore, Tamil Nadu", "January 2017", "June 2017"))
    return experienceDetails


@app.route('/')
def index():
    return jsonify(getExperienceDetails())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
