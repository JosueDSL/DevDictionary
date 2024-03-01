from flask import Blueprint, render_template, request, redirect 

views = Blueprint("views", __name__)

@views.route("/home")
def home():
    return "home"

def hello():
    return "hello"
