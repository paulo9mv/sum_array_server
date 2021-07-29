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
        response = generateError("'arr' prop is missing")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 400

    arr = content['arr']

    # Check if 'arr' is a list
    if isinstance(arr, list):
        # Check if 'arr' contains only integers
        if all(isinstance(elem, int) for elem in arr):
            a = getIndexOfEquilibrium(arr)
            response = jsonify({"index":a})
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        else:
            response = generateError("only integer numbers are allowed")
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 400
    else:
        response = generateError("array is expected")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 400

def generateError(msg):
    return jsonify({"error": msg})