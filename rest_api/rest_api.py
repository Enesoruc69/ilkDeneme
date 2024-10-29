from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class IkiTopla(Resource):
    def get(self):
        sonuc = 2 + 2
        return {'sonuc': sonuc}, 200

class Carp(Resource):
    def post(self):
        veri = request.get_json()
        sayilar = veri.get('sayilar', [])
        sonuc = 1
        for sayi in sayilar:
            sonuc *= sayi
        return {'sonuc': sonuc}, 200

api.add_resource(IkiTopla, '/iki_topla')
api.add_resource(Carp, '/carp')

