#!/usr/bin/python
 
import BaseHTTPServer
import CGIHTTPServer
 
PORT = 6060
server_address = ("", PORT)

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print "Service Web Actif Numero de port :", PORT

httpd = server(server_address, handler)
httpd.serve_forever()

