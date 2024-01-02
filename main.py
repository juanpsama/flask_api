from flask import Flask, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy

from models import User, Product, Category, db

app = Flask(__name__)

# Make that jsonify fuction DON'T order key pairs 
app.json.sort_keys = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cake_store.db'
db.init_app(app)


with app.app_context():

    #If you define models in other modules, you must import them before calling create_all, otherwise SQLAlchemy will not know about them.
    db.create_all()

#TODO: make auth with jwt
#TODO: make a docs page swagger


@app.post('/categories')
def post_categories():
    request_data = request.get_json()
    try:
        new_category = Category(
            title = request_data['title']
        )
    except:

        # If nothing was submitted as the title in request_data['title']
        return jsonify({'error': 'data not found in request'}), 401
    
    db.session.add(new_category)
    db.session.commit()

    return jsonify({'message' : 'Category created succesfuly'}), 201

@app.get('/categories')
def get_categories():
    result = db.session.execute(db.select(Category))
    categories = result.scalars().all()

    # Creates a list with all objects transform in to dictionaries
    results_list = [category.to_dict() for category in categories]
    
    return jsonify(results_list),200

# CRUD products

@app.post('/products')
def post_data():
    request_data = request.get_json()
    try:
        new_product = Product(
            title = request_data['title'],
            description = request_data['description'],
            category_id = request_data['category_id']
        )
    except:

        # If some data is missing to construct the product model in the request
        return jsonify({'error': 'data not found in request'}), 401
    
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message' : 'product created succesfully'}), 201

@app.get('/products')
def get_all_products():
    #TODO: accept queries to filter data in get         
    result = db.session.execute(db.select(Product))
    products = result.scalars().all()

    # Creates a list with all objects transform in to dictionaries
    results_list = [product.to_dict() for product in products]
    
    return jsonify(results_list),200

@app.get('/products/<int:product_id>')
def get_product(product_id):
    try:
        product = db.get_or_404(Product, product_id)
    except:
        return jsonify({"error" : "product not found with that id"}), 404
    
    return jsonify(product.to_dict()),200


@app.delete('/products/<int:product_id>')
def delete_product(product_id):
    try:
        product = db.get_or_404(Product, product_id)
    except:
        return jsonify({"error" : "product not found with that id"}), 404
    
    # Using the db session to delete the product from the database
    db.session.delete(product)
    db.session.commit()    
    return jsonify({'message' : 'product deleted correctly'}), 200


#TODO: Make put and patch entry
@app.put('/')
def put_data():
    return jsonify({'message' : 'hola desde put'})

@app.patch('/')
def patch_data():
    return jsonify({'message' :  'hola desde patch'})

if __name__=='__main__':
    app.run(debug=True)