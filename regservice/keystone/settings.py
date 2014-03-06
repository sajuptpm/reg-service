KEYSTONE_HOST = "127.0.0.1"
KEYSTONE_ADMIN_TOKEN = "openstack"
KEYSTONE_ADMIN_PORT = 35357
KEYSTONE_PUBLIC_PORT = 5000
API_VERSION_V3 = "v3"
KEYSTONE_API_VERSION = API_VERSION_V3

_admin_data = {"host_name":KEYSTONE_HOST, "port":KEYSTONE_ADMIN_PORT, "api_version":KEYSTONE_API_VERSION}
KEYSTONE_ADMIN_ENDPOINT = "http://{host_name}:{port}/{api_version}".format(**_admin_data)
_public_data = {"host_name":KEYSTONE_HOST, "port":KEYSTONE_PUBLIC_PORT, "api_version":KEYSTONE_API_VERSION}
KEYSTONE_PUBLIC_ENDPOINT = "http://{host_name}:{port}/{api_version}".format(**_public_data)

DEFAULT_PROJECT_NAME = "demo"
DEFAULT_ROLE_NAME = "Member"
DEFAULT_DOMAIN_NAME = "Default"
PROJECT_NAME_PREFIX = "project_"


