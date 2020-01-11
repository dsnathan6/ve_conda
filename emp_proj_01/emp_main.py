from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ClsEmp(Resource):
    def get(self, name):
        return {"name of the emp": name}


api.add_resource(ClsEmp, '/emp/<string:name>')
app.run(port=6001)
