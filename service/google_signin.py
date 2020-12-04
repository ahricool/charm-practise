from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route("/v1/signin/internal", methods=["GET", "POST"])
def internal():
    print(request.get_json())
    import ipdb;ipdb.set_trace()

    print("Params:")
    print(request.args.to_dict())
    print("Request body:")
    print(request.get_data())
    print("path:")
    print(request.path)

    if request.method == "POST":
        return "OK"

    print("Please input code:")
    code = str(input())
    code = str(code.strip())
    data = {"data": [
        {"verification": {
            "verification_code": str(code)
        }}
    ]}

    return json.dumps(data)


if __name__ == "__main__":
    app.run(port=8888, debug=True)
