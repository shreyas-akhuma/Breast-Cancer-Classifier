from app import app, inceptionV3
from flask import Flask, render_template, request, redirect, jsonify
from werkzeug.utils import secure_filename
import os

app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png"]
app.config["UPLOAD_PATH"] = "app/static/uploads"

op = {"color" : "inherit", "neutral" : "block", "idc" : "none", "nonidc" : "none", "acc" : "Prediction"}

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/uploader", methods = ["GET", "POST"])
def upload_file():
   global op
   if request.method == "POST":
      if request.form['button'] == "submit":
         f = request.files["file"]
         filename = secure_filename(f.filename)
         if filename != "":
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
               return redirect("/")
            f.save(os.path.join(app.config["UPLOAD_PATH"], filename))
            inceptionV3.classify(f.filename, op)
      elif request.form['button'] == "reset":
         op = {"color" : "inherit", "neutral" : "block", "idc" : "none", "nonidc" : "none", "acc" : "Prediction"}
      return redirect("/")
   elif request.method == "GET":
      return jsonify(op)
