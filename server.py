from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from equilibrium import getIndexOfEquilibrium

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/equilibrium', methods=['patch'])
@cross_origin()
def hello():
    content = request.json

    # Check if 'arr' prop exists
    if 'arr' not in content:
        return jsonify({"error": "'arr' prop is missing"}), 400

    arr = content['arr']

    # Check if 'arr' is a list
    if isinstance(arr, list):
        # Check if 'arr' contains only integers
        if all(isinstance(elem, int) for elem in arr):
            a = getIndexOfEquilibrium(arr)
            return jsonify({"index":a})
        else:
            return jsonify({"error": "only integer numbers are allowed"}), 400
    else:
        return jsonify({"error": "array is expected"}), 400