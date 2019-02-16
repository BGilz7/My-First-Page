from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import EmailForm, LoginForm, RegisterForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = EmailForm()

    return render_template('contact.html', title='Contact Me:', form=form)

@login_required
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user is Logged in already, do not let them access this page
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index'))


    form = LoginForm()

    # check if form is submitted, log user in if so
    if form.validate_on_submit():
        # query the database for the user trying to log in
        user = User.query.filter_by(username=form.username.data).first()

        # if user doesnt exist, reload page and flash messages
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect.')
            return redirect(url_for('login'))

        # if user does exist, and credentials are correct, log them in and send them to their profile page
        login_user(user, remember=form.remember_me.data)
        flash('You are now logged in!')
        return redirect(url_for('index', username=current_user.username))


    return render_template('login.html', title='Login:', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # if user is Logged in already, do not let them access this page
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data
        )

        # set the password hash
        user.set_password(form.password.data)

        # add to stage and commit to db, then flash and return
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register:', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
