import os
from flask import Flask, jsonify, make_response

import utils.response as resp
import utils.query as q
import utils.MetaMap as MetaMap
from utils.ctakes import cTakes
from utils.quickumls import QuickUMLS
from utils.pdf_manager import PdfManager
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
app = Flask(__name__)
