from flask import Flask
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy

from models import User, Product, Categories, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cake_store.db'
db.init_app(app)


with app.app_context():
    
    #If you define models in other modules, you must import them before calling create_all, otherwise SQLAlchemy will not know about them.
    db.create_all()


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