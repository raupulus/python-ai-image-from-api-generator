#! /usr/bin/env python3
import requests
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = os.getenv("DEBUG")
API_UPLOAD = os.getenv("API_URL_CREATE")
API_UPLOAD = os.getenv("API_URL_UPDATE")

class Api:
    def __init__(self):
        self.debug = DEBUG
        self.api_key = os.getenv("API_KEY")
        self.url_create = os.getenv("API_URL_CREATE")
        self.url_update = os.getenv("API_URL_UPDATE")
