from con import Con
from __init__ import *
class PdfManager:
	def __init__(self):
	    self.ip = os.environ.get("MONGO_URL")
	    self.db = os.environ.get("MONGO_DB")
	    self.col = os.environ.get("MONGO_COL")
	    self.port = int(os.environ.get("MONGO_PORT"))

	def _get_pdf(self, doc_id):
	    """Get pdf path based on pdf id
	    Args:
	        doc_id(str): document id 
	    Return:
	        doc_path(str): document storage path
	    """
	    doc_path = None 
	    with Con(db = self.db, host = self.ip, port = self.port, col = self.col) as c:
	        doc = c.find_one({'doc_id': doc_id})
	        doc_path = doc['location'] if doc else None
                print doc_path
	    return doc_path

        def _cov_pdf(self, doc_path):
    	    """Convert pdf into plain text
    	    Args:
    	        doc_path(str): documet path 
    	    Return:
    	        doc_text(str): cleaned content of pdf document
    	    """
            if doc_path:
        	cmd = 'pdf2txt.py ' + doc_path
        	doc_text = subprocess.check_output(cmd, shell = True)
        	doc_text = self._clean(doc_text)
                print doc_text
        	return doc_text
            else:
        	return None

        def _clean(self, doc_text):
    	    """Clean pdf content 
    	    Args:
    	        doc_text(str): pdf content 
    	    Return:
    	        doc_text(str): cleaned pdf content
    	    """
    	    doc_text = doc_text.split("\n")
    	    doc_text = ' '.join(doc_text)
    	    doc_text = ' '.join(doc_text.split())
    	    return doc_text

        def pipeline(self, doc_id):
    	    """Get location, convert and clean
    	    Args:
    	        doc_id(str): id of pdf document 
    	    Return:
    	        doc_text(str): cleaned pdf content
    	    """
            doc_path = self._get_pdf(doc_id)
            doc_text = self._cov_pdf(doc_path)
            return doc_text






