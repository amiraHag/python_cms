from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return 'About Page'


@app.route('/about/<username>')
def about_page_specific_user(username):
    return f'This is the About Page for {username.capitalize()}'


if __name__ == '__main__':
    app.run()
