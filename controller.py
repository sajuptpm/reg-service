
import keystoneapi
import paste
import traceback
from paste.request import parse_formvars
# from db.models import User, DBSession


def create_user(environ):
	"""	
	"""
	#http://pythonpaste.org/do-it-yourself-framework.html
	try:
		if environ['REQUEST_METHOD'] == 'POST':
			fields = parse_formvars(environ)
			password = fields["password"]
			email = fields["email"]
			user = keystoneapi.create_user(email, password, email=email, enabled=False)
			result = {"email": user.email, "enabled": user.enabled, 
						"id": user.id, "name": user.name}
				
			# dbuser = User(email, fields["first_name"], fields["last_name"], email, fields["country"], \
			# 	fields["country_code"], fields["company"], fields["address"], fields["city"], \
			# 	fields["state"], fields["pin"], fields["phone"], user.id, enabled=user.enabled)	
			# DBSession.add(dbuser)
			# DBSession.commit()
		else:
			return {"success":False, "error":"Invalid Request Method", "result":None}
	except Exception as ex:
		#traceback.print_stack()
		#raise ex 
		return {"success":False, "error":str(ex), "result":None}
	return {"success":True, "error":"", "result":result}

def activate_user(environ):
	"""
	"""
	try:
		fields = parse_formvars(environ)##Get&Post data
		args, kwargs  = environ['wsgiorg.routing_args']
		if environ['REQUEST_METHOD'] == 'GET':
			try:
				user_id = kwargs["user_id"]
			except KeyError as ex:
				raise Exception("Argument missing user_id")
			user = keystoneapi.enable_user(user_id)
			result = {"email": user.email, "enabled": user.enabled,
						"id": user.id, "name": user.name}
			# dbuser = DBSession.query(User).filter(User.external_id==user_id).first()
			# if dbuser:
			# 	dbuser.enabled = True
			# 	DBSession.add(dbuser)
			# 	DBSession.commit()
		else:
			return {"success":False, "error":"Invalid Request Method", "result":None}
	except Exception as ex:
		#traceback.print_stack()
		#raise ex 
		return {"success":False, "error":str(ex), "result":None}
	return {"success":True, "error":"", "result":result}





