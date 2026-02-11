"""Create an API that stores revenue from external partners."""

import requests
from flask import Flask, request

api = Flask(__name__)

REVENUE = [
    {"total_revenue": 0},
    {"partner_id": 1,
     "merchant_id": 1,
     "total_amount": 0,
     "count_transactions": 0,
     "currency": "USD",
     "transaction": "SALE",
     "description": "Revenue from partner 1"}
]

@api.route("/")
def index():
    """Return a simple message."""
    return "Welcome to the revenue API!"

@api.route("/revenue", methods=["GET"])
def get_revenue() -> list:
    """Return the total revenue."""
    return REVENUE

@api.route("/revenue", methods=["POST"])
def add_revenue() -> dict:
    """Adds new revenue data to api."""
    new_revenue = request.get_json()
    revenue_keys = [
        "partner_id",
        "merchant_id", 
        "total_amount", 
        "count_transactions",
        "currency", 
        "transaction"
    ]
    if not all(key in new_revenue for key in revenue_keys):
        return {"message": "Missing required fields!"}, 400

    REVENUE.append(new_revenue)
    return {"message": "Revenue added successfully!"}, 201
    


if __name__ == "__main__":
    api.run(port=8080,debug=True, host="0.0.0.0")