from flask import Flask, request


app = Flask(__name__)



@app.route("/api/v1/", methods=['GET'])
def check():
    res = {}
    args = request.args
    url = args.get("url")
    wpcheck = wpcheck(url)
    policycheck = policycheck(url)