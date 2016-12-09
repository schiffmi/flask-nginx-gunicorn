from flask import Blueprint, render_template

mod = Blueprint('home', __name__, static_url_path='/static/client', static_folder='../client/build/')

@mod.route('/home')
def home():
  return render_template('index.html') 