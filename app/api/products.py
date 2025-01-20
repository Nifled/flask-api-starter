from flask import jsonify, make_response, request
from app.api import bp
from app.models import Product
from app import db


@bp.route('/products', methods=['GET'])
def get_products():
  try:
    products = Product.query.all()
    return make_response(jsonify({ 'products': [product.json() for product in products] }), 200)
  except:
    return make_response(jsonify({ 'message': 'Error getting products' }), 500)

@bp.route('/products', methods=['POST'])
def create_product():
  try:
    body = request.get_json()
    name, price, stock_quantity, category_id = body['name'], body['price'], body['stock_quantity'], body['category_id']

    if not name or not price or not stock_quantity:
      return make_response(jsonify({ 'message': 'Missing required fields' }), 400)

    # Create a new product with the provided data
    product = Product(
      name=name, 
      price=price, 
      stock_quantity=stock_quantity, 
      category_id=category_id
    )
    db.session.add(product)
    db.session.commit()

    return make_response(jsonify({ 'message': 'Product created successfully', 'product': product.json() }), 201)
  except Exception as e:
    return make_response(jsonify({ 'message': 'Error creating product', 'error': str(e) }), 500)
