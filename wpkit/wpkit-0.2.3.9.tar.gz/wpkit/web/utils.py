from wpkit import piu
from wpkit import pkg_info
from wpkit.basic import join_path,IterObject,SecureDirPath,PointDict,Path,DirPath,PowerDirPath
from wpkit.basic import render_template as render
from flask import request,render_template,redirect,make_response,jsonify
import functools,inspect
from jinja2 import Environment,PackageLoader
env=Environment(loader=PackageLoader('wpkit.data','templates'))
import inspect

def rename_func(name):
    def decorator(func):
        func.__name__=name
        @functools.wraps(func)
        def new_func(*args,**kwargs):
            return func(*args,**kwargs)
        return new_func
    return decorator

def parse_from(*refers):
    def decorator(f):
        fargs = inspect.getfullargspec(f).args
        @functools.wraps(f)
        def wrapper():
            dic={}
            for ref in refers:
                d = ref() if callable(ref) else dict(ref)
                d = d or {}
                if d:dic.update(d)
            params = {}
            for ag in fargs:
                params[ag] = dic.get(ag, None)
            return f(**params)
        return wrapper
    return decorator
def get_form():return request.form
def get_json():return request.json
def get_cookies():return request.cookies
# parse_json is a decorator
parse_json_and_form=parse_from(get_json,get_form)
parse_json=parse_from(get_json)
parse_form=parse_from(get_form)
parse_cookies=parse_from(get_cookies)
parse_all=parse_from(get_cookies,get_form,get_json)

class UserManager:
    __status_succeeded__='succeeded'
    __status_failed__='failed'
    def __init__(self,dbpath='./data/user_db',home_url='/'):
        self.db=piu.Piu(dbpath)
        self.home_url=home_url
    def status(self,status,**kwargs):
        return jsonify(dict(status=status,**kwargs))
    def home_page(self,**kwargs):
        return env.get_template('pan.html').render(signup=True, **kwargs)
    def signup_page(self,**kwargs):
        return env.get_template('sign3.html').render(signup=True, **kwargs)
    def login_page(self,**kwargs):
        return env.get_template('sign3.html').render(login=True,**kwargs)
    def error_page(self,**kwargs):
        return env.get_template('error.html').render(**kwargs)
    def login_required(self,f):
        @functools.wraps(f)
        @parse_cookies
        def wrapper(user_email,user_password):
            if not (user_email and user_password):
                return self.login_page()
            user=self.db.get(user_email,None)
            user=PointDict.from_dict(user) if user else user
            if user and (user.user_email == user_email ) and (user.user_password==user_password):
                return f()
            else:
                # return self.login_page()
                return self.error_page()
        return wrapper
    def signup(self):
        @parse_form
        def do_signup(user_email,user_password):
            if self.db.get(user_email,None):return self.signup_page(msg='Email has been taken.')
            self.db.add(key=user_email,value={'user_email':user_email,'user_password':user_password})
            resp=make_response(self.status(status=self.__status_succeeded__,redirect=self.home_url))
            resp.set_cookie('user_email',user_email)
            resp.set_cookie('user_password',user_password)
            return resp
        return do_signup()

    def login(self):
        @parse_form
        def do_login(user_email,user_password):
            if not self.db.get(user_email,None):return self.status(self.__status_failed__,msg="Email doesn't exists.")
            resp=make_response(self.home_page())
            resp.set_cookie('user_email',user_email)
            resp.set_cookie('user_password',user_password)
            return resp
        return do_login()





