import os, werkzeug, json
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif'])

parser = reqparse.RequestParser()
parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')

class UploadPic(Resource):
	def post(self):
		args=parser.parse_args()
		picFile = args['file']
		filename = picFile.filename
		if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
			picFile.save("received_image/"+filename)
			return {"code":"200", "desc":"success"}
		else:
			return {"code":"415", "desc":"Unsupported Media Type"}

api.add_resource(UploadPic,'/upload')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5500)
