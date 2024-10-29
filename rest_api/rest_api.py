from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class IkiTopla(Resource):
    def get(self):
        sonuc = 2 + 2
        return {'sonuc': sonuc}, 200



