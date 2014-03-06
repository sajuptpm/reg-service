
import settings
import uuid
import keystoneclient
from keystoneclient.v3 import client


def get_client():
    """
    """
    keystone = client.Client(token=settings.KEYSTONE_ADMIN_TOKEN, 
                    endpoint=settings.KEYSTONE_ADMIN_ENDPOINT)
    return keystone


def _create_user(name, domain=None, project=None, password=None,
                        email=None, description=None, enabled=None,
                        default_project=None, keystone=None, 
                        **kwargs):
    """
    """
    if not keystone:
        keystone = get_client()
    user = keystone.users.create(name, domain=None, project=None, password=password, 
            email=email, description=None, enabled=enabled, default_project=None,
            **kwargs)
    return user


def create_user(name, password, email=None, description=None, enabled=False, **kwargs):
    """
    """
    project = None
    user = None
    role_granted = False
    keystone = get_client()
    _user = get_user_by_name(name)
    if _user:
        raise keystoneclient.apiclient.exceptions.Conflict("User already exist")
    try:
        domain = get_default_domain(keystone) 
        project = create_project(domain, name, keystone)
        role = get_default_role(keystone)
        ##SM:domain is optional
        user = _create_user(name, domain=domain, project=project, password=password, 
            email=email, enabled=enabled, keystone=keystone, **kwargs)
        ##SM:Specify either a domain or project, not both
        keystone.roles.grant(role, user=user, domain=None, project=project)
        role_granted = True
    except Exception as ex:
        if role_granted:
            keystone.roles.revoke(role, user=user, domain=None, project=project)
        if user:
            delete_user(user)
        if project:
            delete_project(project)
        raise ex
    return user


def delete_user(id, keystone=None):
    if not keystone:
        keystone = get_client()
    keystone.users.delete(id)


def create_project(domain, name=None, keystone=None):
    """
    """
    project = None
    if not name:
        name = get_unique_project_name()
    if not keystone:
        keystone = get_client()
    project = keystone.projects.create(name, domain)
    return project


def delete_project(id, keystone=None):
    if not keystone:
        keystone = get_client()
    keystone.projects.delete(id)


def get_unique_project_name():
    """
    """
    project_name = settings.PROJECT_NAME_PREFIX + uuid.uuid4().hex
    while  True:
        project = get_project_by_name(name=project_name)
        if not project:
            break
        project_name = settings.PROJECT_NAME_PREFIX + uuid.uuid4().hex
    return project_name


def get_user_by_name(name, keystone=None):
    user = None
    if not keystone:
        keystone = get_client()
    user_list = keystone.users.list(name=name)
    if user_list:
        user = user_list[0]
    return user


def get_user(id, keystone=None):
    user = None
    if not keystone:
        keystone = get_client()
    user = keystone.users.get(id)
    return user


def get_project_by_name(name=None, project_id=None, keystone=None):
    project = None
    if not keystone:
        keystone = get_client()
    project_list = keystone.projects.list(name=name)
    if project_list:
        project = project_list[0]
    return project

        
def get_default_role(keystone=None):
    role = None
    if not keystone:        
        keystone = get_client()
    role_list = keystone.roles.list(name=settings.DEFAULT_ROLE_NAME)
    if not role_list:
        raise Exception("Could not find the default role:%s"%(settings.DEFAULT_ROLE_NAME))
    else:
        return role_list[0]


def get_default_domain(keystone=None):
    """
    """
    domain = None
    if not keystone:
        keystone = get_client()
    domain = [x for x in keystone.domains.list() if x.name in [settings.DEFAULT_DOMAIN_NAME]]
    if not domain:
        raise Exception("Could not find the default domain:%s"%(settings.DEFAULT_DOMAIN_NAME))
    else:
        return domain[0]


def enable_user(user_id, keystone=None):
    """
    """
    if not keystone:
        keystone = get_client()
    user = keystone.users.update(user=user_id, enabled=True,
            sms_activation_code=None, sms_activation_code_time=None)    
    return user




