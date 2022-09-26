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

if __name__ == "__main__":
  app.run()