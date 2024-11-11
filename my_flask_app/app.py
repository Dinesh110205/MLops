from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Home route with an HTML template
@app.route("/")
def home():
    return render_template("home.html")

# Dynamic route to greet the user by name
@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name.capitalize())

# API route to return JSON data
@app.route("/api/data")
def get_data():
    data = {
        "message": "This is a JSON response",
        "status": "success",
        "data": {"item1": "value1", "item2": "value2"}
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
