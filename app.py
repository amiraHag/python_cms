from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f"Item {self.name}"


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


@app.route('/about/<username>')
def about_page_specific_user(username):
    return f'This is the About Page for {username.capitalize()}'


if __name__ == '__main__':
    app.run()
