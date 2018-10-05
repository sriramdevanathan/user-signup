from flask import Flask, request, render_template, redirect, logging

app = Flask(__name__)
app.config['DEBUG'] = True

u_err=""
pwd_err=""
pwd2_err=""
e_err=""

def validateUN(username):
    global u_err
    if " " in username:
        u_err = "Username cannot contain a space"
        return False
    else:
        if 2 < len(username) < 21:
            u_err = ""
            return True 
        else:
            u_err = "Username must be between 3 and 20 characters"
            return False

def validatePWD(pwd):
    global pwd_err
    if " " in pwd:
        pwd_err = "Password cannot contain a space"
        return False
    else:
        if 2 < len(pwd) < 21:
            pwd_err = ""
            return True 
        else:
            pwd_err = "Password must be between 3 and 20 characters"
            return False

def p_match(pwd, pwd2):
    global pwd_err
    global pwd2_err
    if pwd == pwd2:
        pwd2_err = ""
        return True
    else:
        pwd_err = "Passwords do not match"
        pwd2_err = "Passwords do not match"
        return False

def e_exist(email):
    if len(email) > 0:
        return True
    else:
        e_err = ""
        return False

def e_valid(email):
    global e_err
    if " " in email:
        e_err = "Email cannot contain a space"
        return False
    elif email.count("@") != 1:
        e_err = "Email must contain exactly one @"
        return False
    elif email.count(".") != 1:
        e_err = "Email must contain only one period"
        return False
    else:
        e_err = ""
        return True


@app.route("/")
def index():
    return render_template("signup.html", title="Signup", user_error=u_err, pwd_error=pwd_err, pwd2_error=pwd2_err, email_error=e_err)

@app.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    passwordc = request.form['passwordc']
    email = request.form['email']
    validateUN(username)
    validatePWD(password)
    p_match(password, passwordc)
    exist = e_exist(email)
    valid = e_valid(email)
    if u_err == "" and pwd_err == "" and pwd2_err == "" and e_err == "":
        if not exist:
            return render_template("Welcome.html", title="Welcome", username=username, email=email, user_error=u_err, pwd_error=pwd_err, pwd2_error=pwd2_err, email_error=e_err)
        elif valid:
            return render_template("Welcome.html", title="Welcome", username=username, email=email, user_error=u_err, pwd_error=pwd_err, pwd2_error=pwd2_err, email_error=e_err)
        else:
             return render_template("signup.html", title="Signup", username=username, email=email, user_error=u_err, pwd_error=pwd_err, pwd2_error=pwd2_err, email_error=e_err)
    else:
         return render_template("signup.html", title="Signup", username=username, email=email, user_error=u_err, pwd_error=pwd_err, pwd2_error=pwd2_err, email_error=e_err)

app.run()