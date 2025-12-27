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
