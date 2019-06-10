from wsgiref.simple_server import make_server
from Application import app


serv = make_server("127.0.0.1",8000,app)

print("server start  ....8000")

serv.serve_forever()