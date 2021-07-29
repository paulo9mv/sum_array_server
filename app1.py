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
    if 'arr' not in content:
        return jsonify({"error": "'arr' prop is missing"}), 400

    arr = content['arr']

    if isinstance(arr, list):
        a = getIndexOfEquilibrium(arr)
        return jsonify({"index":a})
    else:
        return jsonify({"error": "array is expected"}), 400