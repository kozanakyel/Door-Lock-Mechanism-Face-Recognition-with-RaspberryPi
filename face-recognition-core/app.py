from flask import Flask
import os
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome Face Recgonition Door lock mechanism</h1>"

@app.route("/start")
def start():
    os.system('python pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle')
    return "<p>start running!</p>"

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
