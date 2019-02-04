from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/signup", methods=['POST'])
def validation():

    username = request.form["username"]
    password = request.form["password"]
    password_conf = request.form["password_conf"]
    email = request.form["email"]
    
    username_error = ""
    password_error = ""
    password_conf_error = ""
    email_error = ""

    if username == "":
        username_error = "Not a valid username"
        username = ""
    elif len(username) <= 3 or len(username) > 20:
        username_error = 'Username out of range (3-20 characters)'
        username = ''
    elif " " in username:
        username_error = "Username cannot contain any spaces"
        username = ""
        
    if password == "": 
        password_error = "Not a valid password"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters long"
    elif " " in password:
        password_error = "Password cannot contain any spaces"
       
    if password_conf == "" or password_conf != password:
        password_conf_error = "Password Must match!"
        password_conf = ""
    
    if email != "":
        if email.count("@") < 1 or email.count("@") > 1:
            email_error = 'Please enter a valid email!'
        if email.count(".") < 1 or email.count(".") > 1:
            email_error = 'Please enter a valid email!'
        if " " in email:
            email_error = "Please enter a valid email!"
        if len(email) < 3 or len(email) > 20:
            email_error = "Email length out of range(3-20)"
    if not username_error and not password_error and not password_conf_error and not email_error:
        return render_template('welcomepage.html', user=username)                                
    else:
        return render_template('homepage.html',
                                username_error=username_error,
                                password_error=password_error,
                                password_conf_error=password_conf_error,
                                email_error=email_error,
                                username=username,
                                email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcomepage.html', user=username)                                



app.run()