import logging, os
import urllib.request
from flask import Flask, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)
#app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3', 'mkv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def custom_response(code, msg):
  response = jsonify({'results':msg})
  response.status_code = code
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/', methods=['GET'])
def homepage():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'files[]' not in request.files:
		return custom_response(400, 'No file part in the request')
	files = request.files.getlist('files[]')
	print(files)
	errors = {}
	success = False
	
	for file in files:		
		if file : #and allowed_file(file.filename):
			fname = os.path.basename(file.filename)
			fpath = os.path.abspath(app.config['UPLOAD_FOLDER'] + file.filename.split(fname)[0])
			if not os.path.isdir(fpath):
				os.makedirs(fpath, exist_ok=True)
			logging.info('filename: ' + fname + ' path: ' + fpath)
			filename = secure_filename(file.filename)
			file.save(os.path.join(fpath, fname))
			success = True
		else:
			errors[file.filename] = 'File type is not allowed'
	
	if success and errors:
		errors['message'] = 'File(s) successfully uploaded'
		return custom_response(206, errors)
	if success:
		return custom_response(201, 'Files successfully uploaded')
	else:
		return custom_response(400, errors)

if __name__ == "__main__":
	# set up your SSL, SSO here
    app.run(host='0.0.0.0', debug=True)