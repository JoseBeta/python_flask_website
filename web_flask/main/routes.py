from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/about_me")
def about_me():
    return render_template('about_me.html')

@main.route("/contact")
def contact():
    return render_template('contact.html')