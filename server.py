import SimpleHTTPServer
import SocketServer
import sys
import os


PORT = 8000

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    pass

Handler.extensions_map['.wasm'] = 'application/wasm'

web_dir = os.path.join(os.path.dirname(__file__), sys.argv[1])
print(web_dir)
os.chdir(web_dir)

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT


try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
