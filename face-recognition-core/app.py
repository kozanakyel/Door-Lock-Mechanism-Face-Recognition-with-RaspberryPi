from flask import Flask, render_template
import os
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/start")
def start():
    os.system('python fc_req_part.py')
    return render_template('index.html')

@app.route("/newuser/<username>")
def newuser(username):
    os.system(f'python headshots.py -n {username}')
    return "<p>New Register!</p>"

@app.route("/encodingfaces")
def encodeFaces():
    os.system('python encode_faces.py --dataset dataset --encodings encodings.pickle --detection-method hog')
    return "<p>Encodeing the faces!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
