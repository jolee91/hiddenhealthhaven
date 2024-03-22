from flask import Flask, request, jsonify, abort
import json

"""
API that serves product information to the company's future mobile app, enabling the app development team to retrieve and display the latest health product data.
"""

app = Flask(__name__)
PRODUCT_CATALOG_FILE = 'product_catalog.json'

def load_product_catalog():
    """Load the product catalog from a JSON file."""
    try:
        with open(PRODUCT_CATALOG_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_product_catalog(catalog):
    """Save the updated product catalog to the JSON file."""
    with open(PRODUCT_CATALOG_FILE, 'w') as file:
        json.dump(catalog, file, indent=4)

@app.route('/products', methods=['GET'])
def get_products():
    """Endpoint to list all products."""
    catalog = load_product_catalog()
    return jsonify(catalog)

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """Endpoint to get details for a specific product."""
    catalog = load_product_catalog()
    product = catalog.get(product_id)
    if product:
        return jsonify(product)
    else:
        abort(404, description="Product not found")

@app.route('/products', methods=['POST'])
def add_or_update_product():
    """Endpoint to add or update a product."""
    product_data = request.json
    product_id = product_data.get('id')
    if not product_id:
        abort(400, description="Product ID is required")

    catalog = load_product_catalog()
    catalog[product_id] = product_data
    save_product_catalog(catalog)

    return jsonify({"message": "Product added/updated successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
