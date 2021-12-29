from flask import Flask, jsonify, request, make_response, render_template
from flask_restful import Resource, Api
from datetime import date 

app = Flask(__name__)
api = Api(app)

def obtainLoggingResponse(log):
    print(f'<<=== LOG : {date.today()} ===>> {log}')
    returnOutput = render_template('index.html')
    return returnOutput

class API(Resource):

	def get(self):
		return make_response(render_template('index.html'), 200, {'Content-Type': 'text/html'})

	def post(self):		
		data = request.get_json()
		return make_response(obtainLoggingResponse(data), 200, {'Content-Type': 'text/html'})

api.add_resource(API, '/')

if __name__ == '__main__':
    app.run(debug = True)
