from flask import Blueprint, render_template

client = Blueprint('client', __name__, 
					static_folder='client-react/build/static/', 
					static_url_path='/static',
					template_folder='client-react/build')

@client.route('/')
def home():
  return render_template('index.html') 