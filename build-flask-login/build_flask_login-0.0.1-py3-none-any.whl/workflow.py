import os
import sys
import shutil
from scripts.messages import empty_name, failure_msg, success_msg
import re

templates_folder = "/templates"
static_folder = "/static"
valid_args_list = ['-d','--debugger', '-cj', '--css-js', '-dC', '--docker-container']

# get application name
def get_app_name():
  try:
      app_name = sys.argv[1]
  except:
      print('App name cannot be empty. Please consider using --help')
      empty_name()
  return app_name

def is_name_valid(app_name):
  # regex to accept only alphanumeric
  if (bool(re.match(r"^[a-zA-Z0-9\-\_]*$", app_name)) and (app_name.startswith('-') is False) and (app_name != "app")):
    return True
  else:
    return False

#get all arguments passed
def get_args():
  args = sys.argv
  args.pop(0)
  return args

def is_args_valid(args):
    valid_args =  all(arg in valid_args_list for arg in args)
    return valid_args

# create directory for application
def create_dir(app_name):
  try:
    os.mkdir(app_name)
  except FileExistsError:
    print('Directory already exists: ' + app_name)
    failure_msg(app_name)

# create app.py in directory 'app_name'
def create_app(app_name):
  appPy = open(app_name + "/app.py", "w+")
  linePython = """
from flask import Flask, render_template
from forms import RegisterForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Enter a secret secret key here!!'

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/register')
def register():
	register_form = RegisterForm()
	return render_template('register.html', title='Register', form=register_form)

@app.route('/login')
def login():
	login_form = LoginForm()
	return render_template('login.html', title='Login', form=login_form)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
    """
  appPy.writelines([linePython])
  appPy.close()

def create_forms(app_name):
  formsPy = open(app_name + "/forms.py", "w+")
  formsPyLines = """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')  
"""
  formsPy.writelines(formsPyLines)
  formsPy.close()

# create templates folder in directory
def create_templates_folder(app_name):
  os.makedirs(app_name + templates_folder)
  lineHtml = """
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World!!</h1>
    <a href='/register'>Register</a>
    <a href='/login'>Login</a>
  </body>
</html>
"""
  indexHtml = open(app_name + templates_folder + "/index.html", "w+")
  indexHtml.writelines([lineHtml])
  indexHtml.close()
  registerHtmlLines = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{ title }}</title>
</head>
<body>
    <form method="POST" action="/">
        {{ form.hidden_tag() }}

        {{ form.username.label }}
        {{ form.username }}
        
        {{ form.email.label }}
        {{ form.email }}
        
        {{ form.password.label }}
        {{ form.password }}

        {{ form.confirm_password.label }}
        {{ form.confirm_password }}

        {{ form.submit }}
    </form>
</body>
</html>
"""
  registerHtml = open(app_name + templates_folder + "/register.html", "w+")
  registerHtml.writelines([registerHtmlLines])
  registerHtml.close()

  loginHtmlLines = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{ title }}</title>
</head>
<body>
    <form method="POST" action="/">
        {{ form.hidden_tag() }}

        {{ form.username.label }}
        {{ form.username }}
        
        {{ form.password.label }}
        {{ form.password }}

        {{ form.submit }}
    </form>
</body>
</html>  
"""

  loginHtml = open(app_name + templates_folder + "/login.html", "w+")
  loginHtml.writelines([loginHtmlLines])
  loginHtml.close()