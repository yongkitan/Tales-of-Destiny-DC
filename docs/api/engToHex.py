from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib.parse import urlparse
import json
from .scripts.eHex import eHex


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)
        parsed_path = urlparse(self.path)
        converted = eHex(data['input'])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version,
            'body': converted}).encode())
        return
