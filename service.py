from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from classes import Phi

app = Flask(__name__)
api = Api(app)

api.add_resource(Phi, '/phi/<n>')

if __name__ == '__main__':
     app.run(port='5001')
