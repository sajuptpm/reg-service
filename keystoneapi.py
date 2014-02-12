
import config_settings

import keystoneclient
from keystoneclient.v3 import client


def get_client():
	"""
	"""
	keystone = client.Client(token=config_settings.KEYSTONE_ADMIN_TOKEN, 
					endpoint=config_settings.KEYSTONE_ADMIN_ENDPOINT)
	return keystone

def _create_user(name, domain=None, project=None, password=None,
                        email=None, description=None, enabled=None, default_project=None, keystone=None):
	"""
	"""
	if not keystone:
		keystone = get_client()
	user = keystone.users.create(name, domain=None, project=None, password=password, 
			email=email, description=None, enabled=enabled, default_project=None)
	return user

def create_user(name, password, email=None, description=None, enabled=False):
	"""
	"""
	keystone = get_client()
	domain = get_default_domain(keystone) 
	project = create_project(email, domain, keystone)
	role = get_default_role(keystone)
	try:
		##SM:domain is optional
		user = _create_user(name, domain=domain, project=project, password=password, 
			email=email, enabled=enabled, keystone=keystone)
	except keystoneclient.apiclient.exceptions.Conflict:
		raise Exception("User already exist")
	##SM:Specify either a domain or project, not both
	keystone.roles.grant(role, user=user, domain=None, project=project)
	return user

def create_project(name, domain, keystone=None):
	"""
	"""
	project = None
	if not keystone:
		keystone = get_client()
	project = keystone.projects.create(name, domain)
	return project


def get_default_project(keystone=None):
	"""
	"""
	project = None
	if not keystone:
		keystone = get_client()
	project = [x for x in keystone.projects.list() if x.name in [config_settings.DEFAULT_PROJECT_NAME]]
	if not project:
		raise Exception("Could not find the default project:%s"%(config_settings.DEFAULT_PROJECT_NAME))
	else:
		return project[0]
		
def get_default_role(keystone=None):
	"""
	"""
	role = None
	if not keystone:		
        	keystone = get_client()
	role = [x for x in keystone.roles.list() if x.name in [config_settings.DEFAULT_ROLE_NAME]]
	if not role:
		raise Exception("Could not find the default role:%s"%(config_settings.DEFAULT_ROLE_NAME))
	else:
		return role[0]

def get_default_domain(keystone=None):
        """
        """
        domain = None
        if not keystone:
                keystone = get_client()
        domain = [x for x in keystone.domains.list() if x.name in [config_settings.DEFAULT_DOMAIN_NAME]]
        if not domain:
                raise Exception("Could not find the default domain:%s"%(config_settings.DEFAULT_DOMAIN_NAME))
        else:
                return domain[0]

def enable_user(user_id, keystone=None):
	"""
	"""
        if not keystone:
                keystone = get_client()
	user = keystone.users.update(user=user_id, enabled=True)	
	return user




