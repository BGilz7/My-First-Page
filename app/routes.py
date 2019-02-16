from app import app
from flask import render_template, url_for, redirect
from app.forms import EmailForm
from app.models import Email

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = EmailForm()

    return render_template('contact.html', title='Contact Me:', form=form)
