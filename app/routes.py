from flask import Blueprint, request, jsonify
from app.models import Data
from app import db

data_routes = Blueprint("data_routes", __name__)


@data_routes.route("/data", methods=["POST"])
def insert_data():
    data = request.json  # Assuming JSON data is sent for insertion
    new_data = Data(name=data.get("name"))

    current_data = Data.query.filter_by(name=data.get("name")).first()
    if current_data:
        return {"message": "Data already exists"}, 409

    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message": "Data inserted successfully"})


@data_routes.route("/data", methods=["GET"])
def get_all_data():
    data_list = [{"id": data.id, "name": data.name} for data in Data.query.all()]
    return jsonify(data_list)


@data_routes.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    element_to_delete = Data.query.get(id)
    if not element_to_delete:
        return {"message": "Data not found"}, 404

    db.session.delete(element_to_delete)
    db.session.commit()
    return {"message": "Data deleted successfully"}


@data_routes.route("/data/<int:data_id>", methods=["PUT"])
def update_data(data_id):
    data = Data.query.get(data_id)

    if not data:
        return jsonify({"error": "Data not found"}), 404

    body = request.get_json()

    if "name" in body:
        data.name = body["name"]

    db.session.commit()

    return jsonify({
        "id": data.id,
        "name": data.name,
        "message": "Data updated successfully"
    })
