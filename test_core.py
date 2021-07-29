import json
import unittest
import numpy as np

from app import app

app.testing = True

class TestApi(unittest.TestCase):

    # Check if statusCode return is correctly when array is OK
    def test_start(self):
        with app.test_client() as client:
            result = client.post(
                '/equilibrium',
                json={"arr":[10,9,10]}
            )
            self.assertEqual(200, result.status_code)

    # Check if the { "arr" } prop exists
    def test_missing_arguments(self):
        with app.test_client() as client:         
            result = client.post(
                '/equilibrium',
                json={"other_value":[10,9,10]}
            )
            self.assertEqual(400, result.status_code)

    # Check if array is valid (array of numbers)
    def test_invalid_array(self):
        with app.test_client() as client:
            result = client.post(
                '/equilibrium',
                json={"other_value":"not an array"}
            )
            self.assertEqual(400, result.status_code)

    # Check the equilibrium index on a big array
    def test_big_array_has_index(self):
        with app.test_client() as client:
            big_array = np.ones(99999, dtype=int).tolist()

            result = client.post(
                '/equilibrium',
                json={"arr":big_array}
            )
            self.assertEqual(49999, json.loads(result.data)['index'])

    # Check when an equilibrium index does not exist
    def test_array_no_index(self):
        with app.test_client() as client:
            big_array = np.ones(100,dtype=int).tolist()

            result = client.post(
                '/equilibrium',
                json={"arr":big_array}
            )
            self.assertEqual(-1, json.loads(result.data)['index'])
            
