from flask import Flask

app = Flask(__name__)

@app.route("/start")
def hello_world():
    import fc_req_part
    return "<p>start running!</p>"