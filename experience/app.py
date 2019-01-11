from flask import Flask
from flask import jsonify
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
    role.append("Working on Associate Android App for Easing workflow for Lowe's Store Employees and Consumer App feature improvements.")
    role.append("Working on Service Virtualization tool based on Wiremock.")
    return role

def appviewxRole():
    role = []
    role.append("Worked on Automation Tools such as Jenkins. Contributed on scripts for AppViewX Product.")
    role.append("Integrated ITSM Tools such as ServiceNow, Jira and Alarm Aggregation System PagerDuty.")
    role.append("Automation and Integration of AWS and VMWare with the product.")
    return role

def webServicesRole():
    role = []
    role.append("Worked on Designing websites for the company's clients.")
    return role

def webarchRole():
    role = []
    role.append("Worked as Lead Full Stack Developer for several college projects.")
    return role

def getExperienceDetails():
    experienceDetails = []
    experienceDetails.append(createDetails("Lowe's India", "Software Engineer", lowesJobRole(), "Bangalore, India", "August 2017", "Present"))
    experienceDetails.append(createDetails("AppViewX / Payoda", "DevOps Engineering Intern", appviewxRole(), "Coimbatore, Tamil Nadu", "January 2017", "June 2017"))
    experienceDetails.append(createDetails("Web Services Jugaad", "Web Designer Intern", webServicesRole(), "Delhi", "May 2015", "July 2015"))
    experienceDetails.append(createDetails("Webarch (SRM University's Technical Club)", "Web Developer Lead", webarchRole(), "Chennai, Tamil Nadu", "September 2013", "May 2017"))
    return experienceDetails

@app.route('/')
def index():
    return jsonify(getExperienceDetails())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')