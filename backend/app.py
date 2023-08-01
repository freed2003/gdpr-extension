from flask import Flask, make_response, request
from api import wpcheck, policycheck

app = Flask(__name__)



@app.route("/api/v1/", methods=['GET'])
def check():
    res = {}
    args = request.args
    url = args.get("url")
    wpcheck = wpcheck(url)
    policycheck = policycheck(url)
    return res

@app.after_request
def cors_yeeter(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
