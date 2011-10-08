from datetime import datetime, timedelta
import re, urllib, cgi, logging
from BaseHTTPServer import BaseHTTPRequestHandler
import storage

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = re.split("[\?\&#]", urllib.unquote(self.path))
        path = url[0]
        vars = dict([x.split('=') for x in url if '=' in x])

        self.send_response(200)
        self.send_header('Content-type',    'text/plain')
        self.end_headers()

        if path == '/digest':
            if 'min' in vars:
                digest = storage.TREE.get_digest([int(vars['min'])])
            else:
                digest = storage.TREE.get_digest([10, 60, 240, 1440, 2880])
            self.wfile.write({'digest': digest})

        if path == '/pattern':
            if 'min' in vars and 'hash' in vars:
                td = datetime.now() - timedelta(minutes=int(vars['min']))
                hash = int(vars['hash'])
                self.wfile.write(storage.TREE.get_details(hash, td))

        if path == '/data':
            if 'hash' in vars and 'host' in vars and 'min' in vars:
                td = datetime.now() - timedelta(minutes=int(vars['min']))
                hash = int(vars['hash'])
                host = vars['host']
                self.wfile.write(storage.TREE.get_host_data(hash, host, td))

        if path == '/patterns/all/':
            self.wfile.write(storage.get_raw_patterns())


    def do_POST(self):
        url = re.split("[\?\&#]", urllib.unquote(self.path))
        path = url[0]
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        if path == "/patterns/save/":
            if 'data' in postvars:
                storage.save_patterns(postvars['data'][0])

        self.send_response(200)
        self.send_header('Content-type',    'text/plain')
        self.end_headers()
        self.wfile.write("OK")

    def log_message (self, format, *args):
        logging.info("%s %s", self.address_string (), format % args)

    def log_error (self, format, *args):
        logging.info("%s %s", self.address_string (), format % args)

    def handle(self):
        try:
            BaseHTTPRequestHandler.handle(self)
        except Exception:
            logging.error("Backend crash", exc_info=1)

