from gevent.wsgi import WSGIServer
from flaskr import app

http_server = WSGIServer(('', 5000), app)
print("gevent server of flask is running ...")
http_server.serve_forever()
