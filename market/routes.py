from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', page_title='Home Page')


@app.route('/shop')
def shop_page():
    items = Item.query.all()
    return render_template('shop.html', shop_items=items, page_title='Shop Page')


@app.route('/about')
def about_page():
    return render_template('about.html', page_title='About Page')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(user_name=form.username.data,
                              email_address=form.email.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('shop_page'))
    if form.errors != {}:
        for err_message in form.errors.values():
            flash(f' There was an error in creating a User {err_message} ', category='danger')

    return render_template('register.html', form=form, page_title='Register Page')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(user_name=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.user_name}', category='success')
            return redirect(url_for('shop_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form, page_title='Login Page')


@app.route('/about/<username>')
def about_page_specific_user(username):
    return render_template('about.html', page_title=f'{username.capitalize()} User Page')