from flask import Flask
from flask.ext.restful import Api
import logging
from logging.handlers import RotatingFileHandler
from keystone.views import UserAPI, UserActivationAPI

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

#http://flask.pocoo.org/docs/errorhandling/?highlight=logging
#https://gist.github.com/ibeex/3257877
handler = RotatingFileHandler('log/service.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

api.add_resource(UserAPI, '/users', '/users/<string:user_id>')
api.add_resource(UserActivationAPI, '/users/<string:user_id>/activate')

if __name__ == '__main__':
    app.run()

