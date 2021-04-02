from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)

class LoginForm(FlaskForm):
    email = StringField(label = 'Email', validators=[DataRequired(), Email(message="Not a valid email")])
    password = PasswordField(label = 'Password', validators=[DataRequired(), Length(min = 8, message="Password should be atleast 8 characters in length")])
    submit = SubmitField(label = "Log in")



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    
    return render_template('login.html', form = login_form )

if __name__ == '__main__':
    app.run(debug=True)