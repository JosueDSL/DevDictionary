from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from . import db
from .models import User

views = Blueprint("views", __name__)

@views.route("/home")
@login_required
def home():
    return "home"

def hello():
    return "hello"
