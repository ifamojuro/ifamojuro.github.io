from flask import render_template, send_file
from .app import app


@app.route("/")
def index():
    return render_template("home.html")

"""
@app.route("/resume")
def res():
       return send_file("static\ife_res.pdf", attachment_filename="resume.pdf")
"""