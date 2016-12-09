from flask import Flask
from .views import home
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(home.mod)

# Default Config
app.config.from_object('config.default')
# Instance Configuration
app.config.from_pyfile('config.py')
# Load file specified by APP_CONFIG_FILE envvar (absolute path)
#app.config.from_envvar('APP_CONFIG_FILE')


#toolbar = DebugToolbarExtension(app)

@app.route('/')
def index():
  return '<html><head><title>Yolo</title></head><body><h1>Yolo</h1></body></html>'

@app.route('/gfb')
def gfb():
  return 'Wow'


for rule in app.url_map.iter_rules():
  print(rule)
