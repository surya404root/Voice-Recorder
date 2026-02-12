from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "recordings"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    audio = request.files.get("audio")
    task = request.form.get("task")

    if audio and task:
        filename = f"task_{task}_{datetime.now().strftime('%H%M%S')}.webm"
        audio.save(os.path.join(UPLOAD_FOLDER, filename))
        return "OK"

    return "Error", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
