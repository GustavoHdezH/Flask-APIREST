from flask import Flask, jsonify, request
from products import products
from app import app

@app.route('/products')
def get_products():
    return jsonify({"products": products, "message":"List of products" })

@app.route('/products/<string:product_name>')
def get_product(product_name):
    product_found =[product for product in products 
                    if product['name'] == product_name ]
    if (len(product_found) >0):
        return jsonify({"product": product_found[0]})
    return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def add_product():
    new_product ={
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity'],
        "quality": request.json['quality']
    }
    products.append(new_product)
    return jsonify({"message":"Product Added Sucesafylly",
                     "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def update_produt(product_name):
    product_found =[product for product in products 
                    if product['name'] == product_name]
    if (len(product_found) > 0):
        product_found[0]['name']= request.json['name']
        product_found[0]['price']= request.json['price']
        product_found[0]['quantity']= request.json['quantity']
        product_found[0]['quality'] = request.json['quality']
        return jsonify ({
            "message": "Product updated",
            "product": product_found[0]
       })
    return jsonify({"message":"Product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    product_found =[product for product in products 
                    if product['name'] == product_name]
    if len(product_found) > 0:
        products.remove(product_found[0])
        return jsonify({
            "message": "Product deleted",
            "product": products
        })
    return jsonify({"message":"Product not found"})
