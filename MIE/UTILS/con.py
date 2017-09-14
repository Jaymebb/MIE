import pymongo

class Con(object):
    def __init__(self, db, host, port, col):
        """Initialize connection"""
        self._client = pymongo.MongoClient(host, port)
        self._col = self._client[db][col]

    def __enter__(self):
        """Get colleciton instance"""
        return self._col

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection"""
        self._client.close()
