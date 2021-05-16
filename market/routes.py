from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm


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


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form, page_title='Register Page')


@app.route('/about/<username>')
def about_page_specific_user(username):
    return f'This is the About Page for {username.capitalize()}'