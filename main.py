from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.get('/')
def get_data():
    return jsonify({'message' : 'Hola desde get'})

@app.post('/')
def post_data():
    return jsonify({'message' : 'Hola desde post'})

@app.delete('/')
def delete_data():
    return jsonify({'message' : 'hola desde delete'})

@app.put('/')
def put_data():
    return jsonify({'message' : 'hola desde put'})

@app.patch('/')
def patch_data():
    return jsonify({'message' :  'hola desde patch'})



if __name__=='__main__':
    app.run(debug=True)