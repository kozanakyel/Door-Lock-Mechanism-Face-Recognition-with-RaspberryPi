from flask import Flask, render_template, request
import os
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/start", methods=['GET'])
def start():
    os.system('python fc_req_part.py')
    return render_template('index.html')

@app.route("/newuser", methods=['POST'])
def newuser():
    user = request.form['username']
    os.system(f'python headshots.py -n {user}')
    return render_template('index.html')

@app.route("/encodingfaces", methods=['GET'])
def encodeFaces():
    os.system('python encode_faces.py --dataset dataset --encodings encodings.pickle --detection-method hog')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
