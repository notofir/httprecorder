from flask import Flask, request

app = Flask(__name__)


@app.route("/reset")
def reset():
    open("data.txt", "w").close()
    return "Data reset."


@app.route("/", methods=["GET", "POST"])
def home():
    result = "<html><body><table>"
    with open("data.txt", "a") as file:
        file.write("<tr><td>" + str(request) + "</td><td>" + str(request.headers) + "</td><td>" + str(request.args) + "</td></tr>")

    with open("data.txt", "r") as file:
        result += file.read()

    result += "</table></body></html>"
    return result
