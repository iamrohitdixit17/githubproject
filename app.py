from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/departments")
def departments():
    return render_template("departments.html")

@app.route("/admissions")
def admissions():
    return render_template("admissions.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        with open("messages.txt", "a") as file:
            file.write(f"{name}, {email}, {message}\n")

        return "Thank you for contacting ABES Engineering College!"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
