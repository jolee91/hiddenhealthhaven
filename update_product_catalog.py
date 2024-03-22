import json
from datetime import datetime

"""
Script to update the product catalog with new health products or changes to existing ones, ensuring all product details are current.
"""

# Sample product catalog file path
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

def update_product(catalog, product_id, product_details):
    """Update or add a product in the catalog."""
    catalog[product_id] = product_details

def remove_product(catalog, product_id):
    """Remove a product from the catalog."""
    if product_id in catalog:
        del catalog[product_id]

def main():
    # Load the existing catalog
    catalog = load_product_catalog()

    # Example updates
    # Adding or updating products
    update_product(catalog, '001', {'name': 'Vitamin C Gummies', 'price': '19.99', 'description': 'Tasty orange-flavored vitamin C gummies.', 'stock': 100})
    update_product(catalog, '002', {'name': 'Detox Tea', 'price': '15.99', 'description': 'Herbal tea for detox and relaxation.', 'stock': 50})

    # Removing a product
    remove_product(catalog, '003')  # Assume product '003' exists in the catalog

    # Save the updated catalog
    save_product_catalog(catalog)

    print(f"Product catalog updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
