import logging

from flask import Flask, jsonify, send_file
from flask_cors import CORS

NAME = "Himanshu Kumar"
NAME_PARAM = "name"
EMAIL = "himanshu.kumar133@gmail.com"
EMAIL_PARAM = "email"
DOB = "July 29, 1995"
DOB_PARAM = "dob"
CONTACT = "+91-8056286756"
CONTACT_PARAM = "contact"
IMAGE_PARAM = "profileImage"
IMAGE = "profile.jpg"
LINKEDIN_PARAM = "linkedIn"
GITHUB_PARAM = "github"
LINKEDIN = "https://www.linkedin.com/in/himanshu-kumar-57864196"
GITHUB = "https://github.com/justsimplify"

app = Flask(__name__)
CORS(app)


def getDetails():
    details = dict()
    details[NAME_PARAM] = NAME
    details[EMAIL_PARAM] = EMAIL
    details[DOB_PARAM] = DOB
    details[CONTACT_PARAM] = CONTACT
    details[IMAGE_PARAM] = "/getImage"
    details[LINKEDIN_PARAM] = LINKEDIN
    details[GITHUB_PARAM] = GITHUB
    return details


@app.route('/')
def index():
    return jsonify(getDetails())


@app.route('/getImage')
def getProfileImage():
    return send_file(IMAGE, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
