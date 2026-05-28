from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Mock data store simulating a backend database state for pipeline validation
MOCK_DB = {
    1: {"id": 1, "task": "Configure Automated Pipeline", "status": "In Progress"}
}

@app.route('/')
def home():
    return jsonify({
        "status": "success", 
        "message": "DevOps Pipeline is working perfectly!",
        "environment": os.getenv("APP_ENV", "production")
    })

# CREATE PATH
@app.route('/items', methods=['POST'])
def create_item():
    return jsonify({"status": "created", "data": MOCK_DB[1]}), 201

# RETRIEVE PATH
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"status": "success", "data": list(MOCK_DB.values())}), 200

# UPDATE PATH
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return jsonify({"status": "updated", "message": f"Item {item_id} modified successfully"}), 200

# DELETE PATH
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return jsonify({"status": "deleted", "message": f"Item {item_id} removed from stack"}), 200

# MONITORING HEALTH PATH
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-api-crud",
        "database": "mock_connected"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)