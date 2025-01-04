from flask import Blueprint, jsonify, request
from models import db, Product

bp = Blueprint("product_routes", __name__, url_prefix="/products")

# Add a new product
@bp.route("/", methods=["POST"])
def add_product():
    data = request.json
    product = Product(
        name=data["name"],
        category=data["category"],
        stock_level=data["stock_level"],
        reorder_point=data["reorder_point"]
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully!"}), 201

# Get all products
@bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "category": p.category,
        "stock_level": p.stock_level,
        "reorder_point": p.reorder_point
    } for p in products])

# Update a product
@bp.route("/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    data = request.json
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.stock_level = data.get("stock_level", product.stock_level)
    product.reorder_point = data.get("reorder_point", product.reorder_point)
    db.session.commit()
    return jsonify({"message": "Product updated successfully!"})

# Delete a product
@bp.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully!"})
