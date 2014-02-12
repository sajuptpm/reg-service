from paste import httpserver
from paste.deploy import loadapp


#SECURITY_SERVICE_HOST = "127.0.0.1"
SECURITY_SERVICE_HOST = "127.0.0.1"
SECURITY_SERVICE_PORT = 8080
httpserver.serve(loadapp('config:config.ini', relative_to='.'),
                     host=SECURITY_SERVICE_HOST, port=SECURITY_SERVICE_PORT)

