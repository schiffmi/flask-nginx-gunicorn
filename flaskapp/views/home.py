from flask import Blueprint

mod = Blueprint('home', __name__)

@mod.route('/<string:page>')
def home(page):
  return '{}!'.format(page)
