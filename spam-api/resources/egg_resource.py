from flask_restful import Resource, fields, marshal

class Egg:
    pass

resources = {
    'type' : fields.String(),
    'cook' : fields.String()
}

class EggResource(Resource):
	
    def get(self):
        e = Egg()
        e.type = 'Chicken'
        e.cook = 'Scrambled'
        return marshal(e,resources)
