import unittest
from flask import Flask
from flask.testing import FlaskClient
from api import app
from algorithms import linear_congruential_generator

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app: Flask = app
        self.client: FlaskClient = app.test_client()
        self.base_url = "http://localhost:5000"

    def test_algorithm_M_endpoint(self):
        X_gen = linear_congruential_generator(2**35, 3141592653, 2718281829, 5772156649)
        Y_gen = linear_congruential_generator(2**35, 2718281829, 3141592653, 1781072418)

        X = [next(X_gen) for _ in range(1000)]
        Y = [next(Y_gen) for _ in range(1000)]

        k = 64
        mod_Y = 35
        n = 100

        url = "/algorithm_M_with_data"
        response = self.client.post(self.base_url + url, json={"X": X, "Y": Y, "k": k, "mod_Y": mod_Y, "n": n})
        print(response.json)
        pass

    def test_algorithm_B_endpoint(self):
        X_gen = linear_congruential_generator(2**35, 3141592653, 2718281829, 5772156649)

        X = [next(X_gen) for _ in range(1000)]

        k = 64
        mod = 35
        n = 100


        response = self.client.post("/algorithm_B_with_data", json={"X": X, "k": k, "mod": mod, "n": n})
        print(response.json)
        pass

    def test_algorithm_M_with_Iterator_endpoint(self):
        k = 64
        n = 100


        response = self.client.post("/alogrithm_M_without_data", json={"aX": 3141592653, "cX": 2718281829, "mX": 35, "seedX": 5772156649, "aY": 2718281829, "cY": 3141592653, "mY": 35, "seedY": 1781072418, "k": k, "n": n})
        print(response.json)
        pass

    def test_algorithm_B_with_Iterator_endpoint(self):
        k = 64
        n = 100


        response = self.client.post("/alogrithm_B_without_data", json={"aX": 3141592653, "cX": 2718281829, "mX": 35, "seedX": 5772156649, "k": k, "n": n})
        print(response.json)
        pass

if __name__ == "__main__":
    unittest.main()