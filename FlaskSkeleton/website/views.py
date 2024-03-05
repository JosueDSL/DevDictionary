from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required
views = Blueprint("views", __name__)

@views.route("/home", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        print('POST Request Received to /home!!!!!!')

    #GET    
    return render_template("home.html")