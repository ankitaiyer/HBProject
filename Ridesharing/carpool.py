from flask import Flask, render_template, redirect, request, flash, url_for, session
import model
#from urlparse import urlparse

app = Flask(__name__)
app.secret_key = "thisispainful"

@app.route("/")
def index():
    # if session.get("email"):
    #     return redirect(url_for("main_menu"))
    # else:
        return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    emailform = request.form.get("email")
    passwordform = request.form.get("password")

    email = model.authenticate(emailform, hash(passwordform))
    if email != None:
        flash("User authenticated!")
        session['email'] = email
    else:
        flash("Password incorrect, please try again.")
    return redirect(url_for("main_menu"))

@app.route("/main_menu")
def main_menu():
    return render_template("main_menu.html")

@app.route("/register")
def register():
    return render_template("register.html")
    
@app.route("/register", methods=["POST"])
def registerUser():
    firstnameform = request.form.get("firstname")
    lastnameform = request.form.get("lastname")
    emailform = request.form.get("email")
    passwordform = request.form.get("password")
    model.register_user(firstnameform,lastnameform,emailform,passwordform)
    return redirect(url_for("index"))

@app.route("/clear_session")
def session_clear():
    session.clear()
    return redirect(url_for("index"))

@app.route("/signup")
def singup():
    return render_template("commute.html")

@app.route("/signup" , methods=["POST"])
def matchfinder():
    if session.get("email"):
        user_id = get_user_by_email(session.get("email"))
    startaddrform = request.form.get("depart")
    destaddrform = request.form.get("destination")
    starttimeform = request.form.get("starttime")
    endtimform = request.form.get("endtime")
    mobileform = request.form.get("mobile")
    workform = request.form.get("work")
    homeform = request.form.get("home")

    


if __name__ == "__main__":
    app.run(debug = True)