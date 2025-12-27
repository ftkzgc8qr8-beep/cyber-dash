import logging
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import shutil
import re
import json
import requests
import feedparser
import cgi

# =======================
# Logging Confirmation
# =======================
logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
#---Four Space Marker
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#---Four Space Marker Check
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch.setFormatter(formatter)
logger.addHandler(ch)
#---Four Space Marker

# =======================
# HTTP Request Handler
# =======================
class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):

    # -------------------------
    # POST: File Upload
    # -------------------------
    def do_POST(self):
        try:
            ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
#---Four Space Marker
            if ctype != 'multipart/form-data':
              self.send_response(400)
              self.end_headers()
              self.wfile.write(b'Invalid Content-Type')
              return
#---Four Space Marker
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ=self.headers,
                keep_blank_values=True
            )  
#----------- Twelve Space Marker
            if 'file' not in form:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'No file field found')
                return
              
