from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from classes import Phi

app = Flask(__name__)
api = Api(app)

api.add_resource(Phi, '/phi/<n>')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response

if __name__ == '__main__':
     app.run(port='5001')
