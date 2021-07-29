import json
import unittest

from app import app

app.testing = True

class TestApi(unittest.TestCase):

    def test_start(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            
            result = client.post(
                '/equilibrium',
                json={"arr":[10,9,10]}
            )
            # check result from server with expected data
            self.assertEqual(200, result.status_code)