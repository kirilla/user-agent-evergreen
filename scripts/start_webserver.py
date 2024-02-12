from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/chrome':
            self.handle_endpoint('chrome.txt')
        elif self.path == '/edge':
            self.handle_endpoint('edge.txt')
        elif self.path == '/firefox':
            self.handle_endpoint('firefox.txt')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def handle_endpoint(self, filename):
        user_agent = self.headers.get('User-Agent', 'Unknown')
        with open(filename, 'w') as file:
            file.write(user_agent + '\n')

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Success')

def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
