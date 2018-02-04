from flask import Flask
from flask_restful import Api

# import all your controllers here
from controllers.egg_controller import *

app = Flask(__name__)
api = Api(app)

# Helpful for debugging your Apache config
print('adding egg')
egg_add(api)
