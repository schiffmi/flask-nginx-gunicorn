from flask import Blueprint, render_template

mod = Blueprint('home', __name__)

@mod.route('/home')
def home():
  return render_template('layout.html') 

@mod.route('/contact')
def contact():
  return render_template('layout.html') 

@mod.route('/about')
def about():
  return render_template('layout.html') 
