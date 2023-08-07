# package imports
import os
from dotenv import load_dotenv

cwd = os.getcwd()
dotenv_path = os.path.join(cwd, os.getenv('ENVIRONMENT_FILE', '.env.development'))
load_dotenv(dotenv_path=dotenv_path, override=True)

APP_HOST = os.environ.get('HOST')
APP_PORT = int(os.environ.get('PORT'))
APP_DEBUG = bool(os.environ.get('DEBUG'))
DEV_TOOLS_PROPS_CHECK = bool(os.environ.get('DEV_TOOLS_PROPS_CHECK'))
API_KEY = os.environ.get('API_KEY', None)
