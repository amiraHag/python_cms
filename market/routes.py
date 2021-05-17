from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db


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
    return 'About Page'


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(user_name=form.username.data,
                              email_address=form.email.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('shop_page'))
    if form.errors != {}:
        for err_message in form.errors.values():
            print(f' There was an error in creating a User {err_message} ')

    return render_template('register.html', form=form, page_title='Register Page')


@app.route('/about/<username>')
def about_page_specific_user(username):
    return f'This is the About Page for {username.capitalize()}'