# utils/settings.py
'''
Load all your settings in here for each access
'''
import os
import dotenv

import utils.constants as c

dotenv_path = os.path.join(c.PATH.CWD, os.getenv('ENVIRONMENT_FILE', '.env.development'))
dotenv.load_dotenv(dotenv_path=dotenv_path, override=True)

_LOADED = False

def load_settings(override=False):
    '''returns true when settings are loaded
    and false when they were already loaded
    '''
    global _LOADED
    if _LOADED and not override:
        return False

    if _host := os.environ.get('DEPLOYMENT_TYPE'):
        c.RUNTIME.DEPLOYMENT_TYPE = _host
    if _host := os.environ.get('HOST'):
        c.RUNTIME.HOST = _host
    if _port := os.environ.get('PORT'):
        c.RUNTIME.PORT = _port
    if _debug := os.environ.get('DEBUG'):
        c.RUNTIME.DEBUG = _debug
    if not (_secret := os.environ.get('SECRET_KEY')):
        raise KeyError('Missing SECRET_KEY in env. Please generate one\n```python\nimport secret\nsecret.token_urlsafe(32)\n```')
    c.RUNTIME.SECRET_KEY = _secret
    _LOADED = True

    return True
