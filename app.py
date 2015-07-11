import os

from flask import Flask
from flask import render_template, render_template_string
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import menu

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
menu.Menu(app=app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
@menu.register_menu(app, '.index', _('Home'), icon="fa-dashboard")
def home():
    return render_template('index.html')

@app.route('/charts')
@menu.register_menu(app, '.charts', 'charts', icon="fa-bar-chart")
def charts_page():
    return render_template('charts.html')


@app.route('/blank')
@menu.register_menu(app, '.blank', 'Blank')
def blank_page():
    return render_template('blank.html')

@app.route('/monkeys')
@menu.register_menu(app, '.monkeys', 'Monkeys', icon="fa-wrench")
def monkeys():
    pass
    # return render_template('monkeys.html')

@app.route('/monkeys/newworld')
@menu.register_menu(app, '.monkeys.newworld', 'New World Monkeys')
def new_world_monkeys():
    return render_template('new_world_monkeys.html')

@app.route('/monkeys/oldworld')
@menu.register_menu(app, '.monkeys.oldworld', 'Old World Monkeys')
def old_world_monkeys():
    return render_template('old_world_monkeys.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
