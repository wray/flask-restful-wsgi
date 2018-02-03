import sys
sys.path.insert(0,'/var/www/apps/spam/spam-api')

from flask import Flask
from flask_restful import Api

# import all your controllers here
from controllers.egg_controller import *

# The variable 'application' is important here, since mod_wsgi will be calling run on that variable
application = Flask(__name__)
api = Api(application)

# Helpful for debugging your Apache config
print('adding egg')
egg_add(api)
