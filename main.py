from flask import Flask, render_template, request
from pytube import YouTube
from pathlib import Path
import os
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download", methods = ["GET", "POST"])
def downloadVideo():
    if request.method == "POST" and "video_url" in request.form:
        youtubeUrl = request.form["video_url"]
        if(youtubeUrl):
            url = YouTube(youtubeUrl)
            video = url.streams.get_highest_resolution()
            downloadFolder = str(os.path.join(Path.home(), "Downloads"))
            video.download(downloadFolder)

    return render_template('index.html')


app.run(debug=True)