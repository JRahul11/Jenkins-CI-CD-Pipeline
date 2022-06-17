from rest_framework.test import APITestCase
from rest_framework import status


class PingCallTest(APITestCase):

    def test_ping(self):
        data = {
                "input": "ping"
            }
        response = self.client.post("/pingpong/", data)
        self.assertEqual(response.data['output'], "pong")

    def test_pong(self):
        data = {
                "input": "pong"
            }
        response = self.client.post("/pingpong/", data)
        self.assertEqual(response.data['output'], "ping")

    def test_pingpong(self):
        data = {
                "input": "pingpong"
            }
        response = self.client.post("/pingpong/", data)
        self.assertEqual(response.data['output'], "pongping")
