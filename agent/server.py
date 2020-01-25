from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json

class WebServerHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        content_type = self.headers['Content-Type']

        if content_type != 'application/json':
            print("Wront content type,json expected!")
            return

        body = self.rfile.read(content_length)
        response = BytesIO()
        response.write(b'Received: ' + body + b'\n')
        self.end_headers()
        self.wfile.write(response.getvalue())

        content_string = body.decode('utf-8')
        content_json_array = json.loads(content_string)
        print(content_json_array)
        # content_dict = {}
        #
        # content_dict['timestamp'] = content_json_array[0]['timestamp']
        # for element in content_json_array['data'][0]:
        #     content_dict['name'] = element['name']
        #     content_dict['cpu'] = element['cpu']
        #     content_dict['memory'] = element['memory']
        #
        # print(content_dict)


    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web server is running on port {}".format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()


if __name__ == '__main__':
    main()