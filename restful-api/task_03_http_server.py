from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30}
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


server = HTTPServer(("localhost", 8000), Handler)
server.serve_forever()
