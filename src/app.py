from flask import Flask, jsonify, request
app = Flask(__name__)


# You are creating a backend software for mobile e-shop app
# Application allows user to purchase various clothing items
# 
# An endpoint is required, which, when requested,
# returns the price + TAX of item.

# =======
# TASK
# =======
# Create an endpoint, which returns a price for items incl. tax. 
# Items with prices can be found in .json file
# Do not forget to create tests for it as well. A basic unit test
# can be found at tests/ folder


TAX = 0.21


@app.route('/price', methods=['GET'])
def price():
    return jsonify(123)
