from flask import Flask, jsonify, request
from products import products
from app import app

@app.route('/test')
def  test():
    return jsonify({"mensaje": "Prueba de script"})
#Petición de general de productos
@app.route('/products')
def get_products():
    return jsonify({"products": products, "message":"List of products" })
#Petición de especifica de producto
@app.route('/products/<string:product_name>')
def get_product(product_name):
    product_found =[product for product in products 
                    if product['name'] == product_name ]
    #print(product_name)
    if (len(product_found) >0):
        return jsonify({"product": product_found[0]})
    return jsonify({"message": "Product not found"})

#Envio de datos
@app.route('/products', methods=['POST'])
def add_product():
    new_product ={
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity'],
        "quality": request.json['quality']
    }
    products.append(new_product)
    #print(request.json)
    """
    Retorna el prodcuto agregado
    """
    return jsonify({"message":"Product Added Sucesafylly",
                     "products": products})

#Actualización de datos
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
    """
    Retorna la optención de un producto para actualizar
    """
    return jsonify({"message":"Product not found"})

#Eliminación de datos
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
    """
    Retorna la optención del producto a eliminar
    """
    return jsonify({"message":"Product not found"})