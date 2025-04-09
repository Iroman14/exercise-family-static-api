import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import Family

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = Family("Jackson")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route("/")
def sitemap():
    return generate_sitemap(app)

@app.route("/members", methods=["GET"])
def get_members():
    members = jackson_family.get_all_members()
    if members is not None:
        print(members)
        return jsonify(members), 200
    else:
        return jsonify({'error': 'Miembros no encotrados'}), 404

@app.route('/members/<int:id>', methods=["GET"])
def get_member(id):
    member = jackson_family.get_member(id)
    if member is not None:
        return jsonify(member), 200
    else:
        return jsonify({'error': 'Miembro no encotrado'}), 407

@app.route('/members/<int:id>', methods=["DELETE"])
def delete_member(id):
    member = jackson_family.get_member(id)
    if member is not None:
        member = jackson_family.delete_member(id)
        return jsonify({'done':True}), 200
    else:
        return jsonify({'error': 'Miembro no encotrado'}), 404

@app.route('/members', methods=["POST"])
def add_member():
    member = request.json
    if member is not None:
        new_member = jackson_family.add_member(member)
        return jsonify(new_member), 200
    else:
        return jsonify({'error': 'Información Invalida'}), 400

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)