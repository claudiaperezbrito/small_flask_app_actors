from flask import Flask, render_template, redirect, url_for, request
from modules import convert_to_dict
from modules import convert_to_dict, make_ordinal

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = '--'


# create a list of dicts
actor_list = convert_to_dict("actors.csv")


# first route

@app.route('/')
def index():
    ids_list = []
    name_list = []
    # fill one list with the number of each presidency and
    # fill the other with the name of each president
    for actor in actor_list:
        ids_list.append(actor['Number'])
        name_list.append(actor['Actor'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(ids_list, name_list)
    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    return render_template('index.html', pairs=pairs_list, the_title="Actors Index")

# second route- this creates the detail page to each actor

@app.route('/actor/<num>')
def detail(num):
    for actor in actor_list:
        if actor['Number'] == num:
            act_dict = actor
            break
    # a little bonus function, imported
    ord = make_ordinal( int(num) )
    return render_template('actor.html', act=act_dict, ord=ord, the_title=act_dict['Actor'])



if __name__ == '__main__':
    app.run(debug=True)
