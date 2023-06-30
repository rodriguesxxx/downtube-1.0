import os
import subprocess
from flask import Flask, request, render_template, redirect, send_file

class Downtube:
    def __init__(self):
        self.url = ""
        self.resolution = ""
        self.output = ""
        self.video_name = ""
        self.state = ""
        self.msg_download_link = ""
    
    def download(self):
        cmd = [
            "yt-dlp",
            "-f",
            "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "-o",
            f"temp_files/{self.video_name}",
            self.url,
        ]
        subprocess.run(cmd)

    def getYtVideoName(self):
        cmd = ["yt-dlp", "-e", self.url]
        output = subprocess.check_output(cmd)
        self.video_name = output.decode().strip()
        return self.getVideoName()

    def getVideoName(self):
        return self.video_name


    def setUrl(self, url):
        self.url = url
    
    def setResolution(self, resolution):
        self.resolution = resolution
    
    def setState(self, state):
        self.state = state

    def getUrl(self):
        return self.url
    
    def getResolution(self):
        return self.resolution
    
    def getState(self):
        return self.state
    def output(self):
        return self.output


app = Flask(__name__, static_folder='static')
dt = Downtube()

@app.route("/")
def redirect_to_site():
    return redirect("/downtube")

@app.route("/downtube")
def downtube():
    video_name = ""
    if(dt.getVideoName() != ""):
        video_name = dt.getVideoName()
        dt.msg_download_link = "Clique aqui para baixar"
        dt.setState(video_name)
    return render_template("index.html", state = dt.getState(), msg_download_link=dt.msg_download_link)

@app.route("/informations", methods=["POST","GET"])
def informations():
    dt.setUrl(request.form["url"])
    dt.getYtVideoName()
    return redirect("/downtube")

@app.route("/prepare")
def prepare_download():
    dt.msg_download_link = ""
    dt.download()
    return redirect("/download")



@app.route("/download")
def download():
    dir_video = f'temp_files/{dt.getVideoName()}.mp4'
    dt.setState("")
    if(os.path.exists(dir_video)):
        resposta = send_file(dir_video, as_attachment=True)
        return resposta
    return ""

@app.route("/delete/<conf>")
def delete(conf):
    if conf == "2004":
        dir_ = "temp_files/"
        files = os.listdir(dir_)
        for file in files:
            os.remove(dir_+file)
        return "delete all files"
    return ""

if "__main__" == __name__:
    app.run(debug=True, host='0.0.0.0')
