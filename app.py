from flask import Flask,render_template,send_from_directory,request
from werkzeug.utils import secure_filename
from json import loads
from os import path as path_
from os import walk

with open('configure.json', 'r') as file:
    configure = loads(file.read())

app = Flask(__name__)
app.template_folder = configure['template_folder']
app.static_folder = configure['static_folder']
app.host = configure['host']
app.port = configure['port']
@app.route('/')
@app.route('/<path:path>')
def index(path=''):
    root_directory = 'documents/{path}'.format(path=path)
    def url(app):
        return 'http://{host}:{port}/'.format(host=app.host,port=app.port)

    if path_.isdir(root_directory):
        for root, dirs, files in walk(root_directory, topdown=False):
            folder = dirs
            file = files
        return render_template('index.html',path=path,folder=folder,file=file,url=url(app))
    else:
        return send_from_directory('documents/', path, as_attachment=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        path = request.form['path']
    except:
        return 'False'
    else:
        file.save('documents/{path}/{file}'.format(path=path,file=secure_filename(file.filename)))
        return 'True'


if __name__=='__main__':
    app.run(host=app.host,port=app.port,debug=True)