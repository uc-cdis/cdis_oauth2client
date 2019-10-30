from flask import Flask
import unittest

app = Flask(__name__)

from cdis_oauth2client import blueprint
app.register_blueprint(blueprint)

class BluePrintTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def test_authorization_url(self):
		response = self.app.get('/authorization_url')
		self.assertEqual(response.status_code, 500)

	def test_do_authorize(self):
		response = self.app.get('/authorize')
		self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
	unittest.main()
