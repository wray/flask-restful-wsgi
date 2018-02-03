from resources.egg_resource import *

def egg_add(api):

    api.add_resource(EggResource,'/api/egg')
