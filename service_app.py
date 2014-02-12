

import controller
import json
import re

def create_user(environ, start_response):
        """
        """
        response_headers = [('Content-type','application/json')]
        status = '200 OK'
        start_response(status, response_headers)
        res = controller.create_user(environ)
        return json.dumps(res)

def activate_user(environ, start_response):
        """
        """
        response_headers = [('Content-type','application/json')]
        status = '200 OK'
        start_response(status, response_headers)
        res = controller.activate_user(environ)
        return json.dumps(res)



##############################

def app_factory(global_config, **local_config):
    """This function wraps our simple WSGI app so it
    can be used with paste.deploy"""
    return dispatch_app


class RegexDispatch(object):
    """
    """
    #http://wsgi.readthedocs.org/en/latest/specifications/routing_args.html
    def __init__(self, patterns):
        self.patterns = patterns

    def __call__(self, environ, start_response):
	"""
	"""
        script_name = environ.get('SCRIPT_NAME', '')
        path_info = environ.get('PATH_INFO', '')
        for regex, application in self.patterns:
            match = regex.match(path_info)
            if not match:
                continue
            extra_path_info = path_info[match.end():]
            if extra_path_info and not extra_path_info.startswith('/'):
                # Not a very good match
                continue
            pos_args = match.groups()
            named_args = match.groupdict()
            cur_pos, cur_named = environ.get('wsgiorg.routing_args', ((), {}))
            new_pos = list(cur_pos) + list(pos_args)
            new_named = cur_named.copy()
            new_named.update(named_args)
            environ['wsgiorg.routing_args'] = (new_pos, new_named)
            environ['SCRIPT_NAME'] = script_name + path_info[:match.end()]
            environ['PATH_INFO'] = extra_path_info
            return application(environ, start_response)
        return self.not_found(environ, start_response)

    def not_found(self, environ, start_response):
        #start_response('404 Not Found', [('Content-type', 'text/plain')])
        start_response('404 Not Found', [('Content-type', 'application/json')])
        return json.dumps(['Not found'])


###### URLS ######
dispatch_app = RegexDispatch([
    (re.compile(r'/users/create$'), create_user),
    (re.compile(r'/users/activate/(?P<user_id>.+)$'), activate_user),
])







