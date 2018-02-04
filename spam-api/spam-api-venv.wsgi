# Requires a virtualenv, spam-venv, to be created at /var/www/apps/spam
activate_this = '/var/www/apps/spam/spam-venv/bin/activate_this.py'
execfile(activate_this,dict(__file__=activate_this))

import sys

sys.path.insert(0,'/var/www/apps/spam3/spam-api')

from flask import Flask
from flask_restful import Api

from controllers.egg_controller import *

application = Flask(__name__)
api = Api(application)

# Helpful for debugging
print('adding egg')
egg_add(api)
