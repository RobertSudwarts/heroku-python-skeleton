from flask import Flask
from flask import render_template_string
from flask.ext import menu

app = Flask(__name__)
menu.Menu(app=app)

def tmpl_show_menu():
    return render_template_string(
        """
        {%- for item in current_menu.children %}
            {% if item.active %}*{% endif %}{{ item.text }}
        {% endfor -%}
        """)

@app.route('/')
@menu.register_menu(app, '.', 'Home')
def index():
    return tmpl_show_menu()

@app.route('/first')
@menu.register_menu(app, '.first', 'First', order=0)
def first():
    return tmpl_show_menu()

@app.route('/second')
@menu.register_menu(app, '.second', 'Second', order=1)
def second():
    return tmpl_show_menu()

@app.route('/third')
@menu.register_menu(app, '.third', 'Third', order=2)
def third():
    return tmpl_show_menu()

if __name__ == '__main__':
    app.run(debug=True)