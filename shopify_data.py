import requests
import json

# Shopify API Credentials
SHOPIFY_STORE = "tgbtgb-8w.myshopify.com"
API_KEY = "0668fdf9b753dfe05b62a63d1a2d1262"
PASSWORD = "9fcdf6a9d7f760721f4b0ad2bb2f41e6"

def get_shopify_data():
    """Fetches product details and orders from Shopify."""
    headers = {"X-Shopify-Access-Token": PASSWORD}

    # Get products
    product_url = f"https://{SHOPIFY_STORE}/admin/api/2023-07/products.json"
    product_response = requests.get(product_url, headers=headers)
    products = product_response.json().get("products", [])

    # Get orders
    order_url = f"https://{SHOPIFY_STORE}/admin/api/2023-07/orders.json"
    order_response = requests.get(order_url, headers=headers)
    orders = order_response.json().get("orders", [])

    # Format product & order data
    product_data = [{"title": p["title"], "description": p["body_html"]} for p in products]
    order_data = [{"order_id": o["id"], "status": o["financial_status"]} for o in orders]

    # Save to file (so AI can use it)
    data = {"products": product_data, "orders": order_data}
    with open("store_data.json", "w") as f:
        json.dump(data, f, indent=4)

    return data

# Fetch data when script runs
if __name__ == "__main__":
    print("Fetching Shopify data...")
    get_shopify_data()
    print("Shopify data saved successfully!")
