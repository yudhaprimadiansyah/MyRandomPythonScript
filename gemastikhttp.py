from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import urllib
import SocketServer

FLAG = "GEMASTIK{}"

class S(BaseHTTPRequestHandler):

    def set_content_type(self, path):
        ext = os.path.splitext(path)[1]
        if (ext == '.png'):
            self.send_header('Content-type', 'image/png')
        elif (ext == '.jpg'):
            self.send_header('Content-type', 'image/jpg')
        else:
            self.send_header('Content-type', 'text/html')

    def do_GET(self):
        path = urllib.unquote(self.path)
        if (path == '/'):
            path = "/index.html"
        path = 'public' + path
        if (os.path.exists(path)):
            f = open(path, 'r').read()
            self.send_response(200)
            self.set_content_type(path)
            self.end_headers()
            self.wfile.write(f)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("<html><body><h1>404 Not Found</h1></body></html>")


def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()


