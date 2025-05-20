from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
load_dotenv()