from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registered", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("classid"):
        return render_template("failure.html")
    else:
        file = open("registrants.csv", "a")
        writer = csv.writer(file)
        writer.writerow((request.form.get("name"), request.form.get("classid")))
        file.close()
        return render_template("success.html")

@app.route("/registrants")
def registrants():
    with open("registrants.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
    return render_template("registrants.html", students=students)