import os
import unittest
import pymongo
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class TestDBConnection(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestDBConnection, self).__init__(*args, **kwargs)
		self.client = pymongo.MongoClient()
		self.MONGO_DB = os.environ.get("MONGO_DB")
		self.MONGO_COL = os.environ.get("MONGO_COL")

	def test_setup(self):
		db = self.client[self.MONGO_DB]
		col = db[self.MONGO_COL]

	def test_teardown(self):
		self.client.close()
    	

if __name__ == '__main__':
    unittest.main()
