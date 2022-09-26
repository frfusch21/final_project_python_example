from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    fileData = 0
    with open('database.json', 'r') as f:
        fileData = json.load(f)
        f.close()
    return render_template("index.html", fileData = fileData)

@app.route("/about", methods=["POST", "GET"])
def about():
    # fileData = 0
    # with open('database.json', 'r') as f:
    #     fileData = json.load(f)
    #     f.close()
    return render_template("about.html")

@app.route("/service", methods=["POST", "GET"])
def service():
    # fileData = 0
    # with open('database.json', 'r') as f:
    #     fileData = json.load(f)
    #     f.close()
    return render_template("service.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    # fileData = 0
    # with open('database.json', 'r') as f:
    #     fileData = json.load(f)
    #     f.close()
    return render_template("contact.html")

if __name__ == "__main__":
  app.run()