from flask import Flask, render_template
from .views import home
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__, instance_relative_config=True)

# Default Config
app.config.from_object('config.default')
# Instance Configuration
app.config.from_pyfile('config.py')
# Load file specified by APP_CONFIG_FILE envvar (absolute path)
#app.config.from_envvar('APP_CONFIG_FILE')


#toolbar = DebugToolbarExtension(app)

app.register_blueprint(home.mod)
@app.route('/')
def index():
    return render_templte('index.html')

for rule in app.url_map.iter_rules():
  print(rule)
