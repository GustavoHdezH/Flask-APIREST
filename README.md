# API REST con Flask

Flask es un framework escrito en python que perimte hacer aplicaciones de una manera rápida y con pocas líneas de código.
Una API es una interfaz grafica para la comunicación entre la aplicación y software que comparten datos entre ellos. Una API puede se publica que implica que cualquiera puede acceder a la informacíon y tambien puede ser privada, lo que implica que requiere autentificación y en la primera autentificación devuelve un token (Objeto contendeor de datos de autentificación), si el token esta vigente no se pide autentificación y el formato para el token es JWT. REST es una arquitectura de desarrollo de APIs y la parte fundamental para el desarrollo de las misma, las operaciones fuandamentales son los metodos HTTP y son 4 GET (permite leer y consultar información), POST (permite crear nueva información), PUT (permite actualizar la información), DELETE (permite eliminar la información).

<p align="center">
<a><img src=https://img.shields.io/badge/version-0.0.2-brightgreen><a>
<a><img src="https://img.shields.io/badge/version%20doc-3.0-brightgreen"></a>
</p>

## Requerimientos

Python 3.8.2 y Flask 1.1.1 son actualmente compatibles con este proyecto.
Tambien se utlizo el software de [Imsomnia][1] para validar y comprobar los metodos HTTP.

[1]: https://insomnia.rest/download/

Adicionalmente se requieren bibliotecas adicionales como jsonify que permite convertir un objeto a un json y la la biblioteca de request la cual permite hacer solicitues HTTP y sean mas simples.

## Instalación

Para instalar la versión estable con **pip**

`$ pip install Flask`

## Importanción de módulos

Importación de módulos

```python
from flask import Flask, jsonify, request
```

Para importar las clases necesarias

```python
from products import products
```

## Inicio rápido

Para este proyecto se va a utilizar un archivo desde el cual se va a extraer la información de una tienda de remate de electronicos, en los cuales se tiene distintos productos para oficina o de uso comun, se puede consultar el precio, la garantia tras salir de la tienda y la calidad del producto selecciónado.

```python
products = [
    {"name":"laptop","price": 900, "quantity":4,"quality": "alta"},
    {"name":"mouse","price": 40, "quantity":2,"quality":"regular"},
    {"name":"monitor","price":400,"quantity":3,"quality":"baja"},
    {"name":"gabinete","price":70 ,"quantity":1,"quality":"baja"}
    ]
```

## Ejemplo

### Bibliotecas requeridas para el funcionamiento correcto

```python
from flask import Flask, jsonify, request
```

### Biblioteca orgien de datos requeridos

```python
from products import products
```

### Estructura inicial del servidor

```python
app = Flask(__name__)

if __name__ == '__main__':
    app.run()
```

### Configuración de servidor para pruebas y puerto especifico

```python
if __name__ == "__main__":
    app.run(debug=True, port=4000)
```

### Función para obener una lista general de productos

```python
@app.route('/products')
def get_products():
    return jsonify({"products": products, "message":"List of products" })
```

### Función para obetener un registo especifico

```python
@app.route('/products/<string:product_name>')
def get_product(product_name):
    product_found =[product for product in products
                    if product['name'] == product_name ]
    if (len(product_found) >0):
        return jsonify({"product": product_found[0]})
    return jsonify({"message": "Product not found"})
```

### Función para agregar un registro

```python
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
```

### Función para actualizar un registro

```python
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
```

### Función para eliminar un registro

```python
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
```

<p align="center">
Codename : Aurora
</p>
<p align="center">
Gustavo Hernandez  |  2020&copy;
</p>