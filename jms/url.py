#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


API_URL_MAPPING = {
    'terminal-register': '/api/terminal/v1/terminal/',
    'terminal-heartbeat': '/api/terminal/v1/terminal/status/',
    'session-replay': '/api/terminal/v1/sessions/%s/replay/',
    'session-command': '/api/terminal/v1/command/',
    'user-auth': '/api/users/v1/auth/',
    'user-assets': '/api/perms/v1/user/%s/assets/',
    'user-asset-groups': '/api/perms/v1/user/%s/asset-groups-assets/',
    'my-profile': '/api/users/v1/profile/',
    'system-user-auth-info': '/api/assets/v1/system-user/%s/auth-info/',
    'validate-user-asset-permission': '/api/perms/v1/asset-permission/user/validate/',
    'finish-task': '/api/terminal/v1/tasks/%s/',
    'asset': '/api/assets/v1/assets/%s/',
    'system-user': '/api/assets/v1/system-user/%s',
}
