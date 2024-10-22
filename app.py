from flask import Flask, jsonify, request
from deltacalculate.maicall import DeltaValue, CreateToken


app = Flask(__name__)

value = DeltaValue()
getToken = CreateToken()
# Sample data to act as our "database"
items = [
    {"id": 1, "name": "Item 1", "price": 15.00},
    {"id": 2, "name": "Item 2", "price": 25.00},
    {"id": 3, "name": "Item 3", "price": 35.00}
]


# create token
@app.route('/createtoken', methods=['POST'])
def create_token():
    data = request.get_json() 
    name= data.get('name')
    id= data.get('userId')
    token= data.get('token')
    msg =getToken.token(name,id,token)
    return msg

#get value
@app.route('/delta/<int:pe>/<int:ce>/<string:expirydate>', methods=['GET'])
def get_itemValue(pe,ce,expirydate):
    item = value.calling(pe,ce,expirydate)
    print(item)
    #item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item.update(updated_item)
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return '', 204

#if __name__ == '__main__':
#    app.run(debug=True)
