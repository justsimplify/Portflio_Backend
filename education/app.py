from flask import Flask
from flask import jsonify
from flask_cors import CORS

NAME_PARAM = "schoolName"
QUALIFICATION_PARAM = "qualification"
CGPA_PARAM = "cgpa"
IS_CGPA = "isCgpa"

app = Flask(__name__)
CORS(app)

def createDetails(name, qualification, cgpa, iscgpa):
    details = dict()
    details[NAME_PARAM] = name
    details[QUALIFICATION_PARAM] = qualification
    details[CGPA_PARAM] = cgpa
    details[IS_CGPA] = iscgpa
    return details

def getCollegeDetails():
    collegeDetails = []
    collegeDetails.append(createDetails("SRM University", "B.Tech in Computer Science", "8.7", True))
    collegeDetails.append(createDetails("Dr. Virendra Swarup Education Centre", "Intermediate", "77.8", False))
    collegeDetails.append(createDetails("Dr. Virendra Swarup Education Centre", "High School", "8.8", True))
    return collegeDetails

@app.route('/')
def index():
    return jsonify(getCollegeDetails())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')