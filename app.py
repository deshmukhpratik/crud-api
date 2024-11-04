from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
]

# Route for the root URL
@app.route('/')
def home():
    return "Welcome to the CRUD API!"

# Read all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Read a single item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    return jsonify(item) if item else ('', 404)

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return ('', 404)
    updated_item = request.get_json()
    item.update(updated_item)
    return jsonify(item)

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
