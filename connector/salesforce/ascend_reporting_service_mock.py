import flask
from flask import request
import json

app = flask.Flask(__name__)


@app.route("/v3.0/organizations/contract_status")
def status():
    print(request.args.to_dict())
    response = {"contract_status": [{
        "ss_organization_id": "Anything*()^*",
        "provision_id": "a1G1s000000E1SZEA0",
        "status": "Active"}]}

    return json.dumps(response)


if __name__ == "__main__":
    app.run(port=5009, debug=True)
