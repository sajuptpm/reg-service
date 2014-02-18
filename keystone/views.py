
from flask import jsonify, request
from flask import current_app
from flask.ext.restful import Resource, reqparse
import keystoneclient
import keystoneapi

#http://flask-restful.readthedocs.org/en/latest/quickstart.html#resourceful-routing
#http://flask.pocoo.org/docs/views/#method-based-dispatching
#http://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful

#http://stackoverflow.com/questions/13284858/how-to-share-the-global-app-object-in-flask

def get_default_error_message():
    return "Unable to process your request.Please contact the site administrator"

class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', type=str)
        self.reqparse.add_argument('password', type=str)
        self.reqparse.add_argument('first_name', type=str)
        self.reqparse.add_argument('last_name', type=str)
        self.reqparse.add_argument('address', type=str)
        self.reqparse.add_argument('country', type=str)
        self.reqparse.add_argument('city', type=str)
        self.reqparse.add_argument('state', type=str)
        self.reqparse.add_argument('pin', type=str)
        self.reqparse.add_argument('phone', type=str)
        self.reqparse.add_argument('company', type=str)
        self.reqparse.add_argument('country_code', type=str)
        self.reqparse.add_argument('sms_activation_code_time', type=str)
        self.reqparse.add_argument('sms_activation_code', type=str)
        super(UserAPI, self).__init__()
        
    def post(self):
        result = None
        args = self.reqparse.parse_args()
        email = args.pop("email")
        password = args.pop("password")
        try:
            user = keystoneapi.create_user(email, password, email=email, enabled=False, **args)
            result = {"email": user.email, "enabled": user.enabled, 
                        "id": user.id, "name": user.name}
        except keystoneclient.apiclient.exceptions.Conflict as ex:
            current_app.logger.exception(ex)
            return {"success":False, "error":"Username already exist", "result":result}
        except Exception as ex:
            #traceback.print_stack()
            current_app.logger.exception(ex)
            return {"success":False, "error":get_default_error_message(), "result":result}
        return {"success":True, "error":"", "result":result}

    def get(self, user_id):
        """
        """
        result = None
        first_name = None
        last_name = None
        address = None
        country = None
        city = None
        state= None
        pin = None
        phone = None
        company = None
        country_code = None
        sms_activation_code_time = None
        sms_activation_code = None

        try:
            user = keystoneapi.get_user(user_id)
            try:
                first_name = user.first_name
            except Exception as e:
                pass
            try:
                last_name = user.last_name
            except Exception as e:
                pass
            try:
                address = user.address
            except Exception as e:
                pass
            try:
                country = user.country
            except Exception as e:
                pass
            try:
                city = user.city
            except Exception as e:
                pass
            try:
                state = user.state
            except Exception as e:
                pass
            try:
                pin = user.pin
            except Exception as e:
                pass
            try:
                phone = user.phone
            except Exception as e:
                pass
            try:
                company = user.company
            except Exception as e:
                pass
            try:
                country_code = user.country_code
            except Exception as e:
                pass
            try:
                sms_activation_code_time = user.sms_activation_code_time
            except Exception as e:
                pass
            try:
                sms_activation_code = user.sms_activation_code
            except Exception as e:
                pass

            result = {"email": user.email, "enabled": user.enabled, 
                        "id": user.id, "name": user.name,
                        "sms_activation_code_time": sms_activation_code_time,
                        "sms_activation_code": sms_activation_code}

            return {"success":True, "error":"", "result":result}
        except Exception as ex:
            current_app.logger.exception(ex)
            return {"success":False, "error":get_default_error_message(), "result":result}

class UserActivationAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(UserActivationAPI, self).__init__()

    def put(self, user_id):
        args = self.reqparse.parse_args()
        try:
            user = keystoneapi.enable_user(user_id)
            result = {"email": user.email, "enabled": user.enabled,
                        "id": user.id, "name": user.name}
        except Exception as ex:
            #traceback.print_stack()
            #raise ex 
            current_app.logger.exception(ex)
            return {"success":False, "error":get_default_error_message(), "result":result}
        return {"success":True, "error":"", "result":result}

