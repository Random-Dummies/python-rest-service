#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
#curl -i -X GET http://localhost:8080
# curl -i -X GET http://localhost:8080
# curl -i -X DELETE http://localhost:8080
# curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://localhost:8080
# curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://localhost:8080

from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        request_path = self.path
        
        print("\n----- Request Start ----->\n")
        print("Request path:", request_path)
        print("Request headers:", self.headers)
        print("<----- Request End -----\n")
        
        self.send_response(200)
        self.send_header("Status", "Green")
        self.end_headers()
        
    def do_POST(self):
        
        request_path = self.path
        
        print("\n----- Request Start ----->\n")
        print("Request path:", request_path)
        
        request_headers = self.headers
        content_length = request_headers.get('Content-Length')
        length = int(content_length) if content_length else 0
        
        print("Content Length:", length)
        print("Request headers:", request_headers)
        payload = self.rfile.read(length)
        print(payload_json)
        #### Insert Code HERE TO CALL NEURAL NET
        print("Request payload:", payload)
        print("<----- Request End -----\n")
        Score = 5
        self.send_response(Score)
        self.end_headers()
    
    do_PUT = do_POST
    do_DELETE = do_GET
        
def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
main()
