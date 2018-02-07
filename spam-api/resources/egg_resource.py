from flask_restful import Resource, fields, marshal

class Egg:
    pass

resources = {
    'type' : fields.String(),
    'cook' : fields.String(),
    'sunny-side' : fields.Boolean(attribute='sunny_side')
}

class EggResource(Resource):
	
    def get(self):
        print('Ordering the egg.')
        e = Egg()
        e.type = 'Chicken'
        e.cook = 'easy'
        e.sunny_side = True
        return marshal(e,resources)
