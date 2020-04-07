from flask import Flask, jsonify, request
from products import products
from app import app


if __name__ == '__main__':
    app.run()