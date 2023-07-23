from flask import Flask, request
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