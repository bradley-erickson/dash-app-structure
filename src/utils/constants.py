'''Constants

Things that have a consistent value across the system
'''
import os
import secrets

# TODO we should build a thing that reads in .js function names

class DEPLOYMENT:
    '''Specific deployment types
    '''
    PRODUCTION = 'production'
    DEV = 'dev'
    TEST = 'test'

class RUNTIME:
    '''utils/settings.py modifies
    this class on settings load
    '''
    HOST = '0.0.0.0'
    PORT = '8000'
    DEBUG = True
    DEPLOYMENT_TYPE = DEPLOYMENT.DEV
    SECRET_KEY = secrets.token_urlsafe(16)

class PATH:
    CWD = os.getcwd()
    ASSETS = 'assets'
    LOGOS = os.path.join(CWD, ASSETS, 'logos')

class TIME:
    '''Common time items
    '''
    SECOND = 1
    MINUTE = SECOND * 60
    HOUR = MINUTE * 60
    HALF_DAY = HOUR * 12
    DAY = HOUR * 24
    WEEK = DAY * 7
    FORTNIGHT = WEEK * 2
    HALF_YEAR = DAY * 183
    YEAR = DAY * 365

class DASH:
    '''Constants used for referencing different component
    attributes - primarly for callbacks.
    This list includes attributes for dash.html, dash.dcc,
    and dash-bootstrap-components.
    '''
    ACTIVE = 'active'
    BASE64_IMAGE_STR = 'data:image/png;base64,{}'
    BLANK = '_blank'
    CHILDREN = 'children'
    CLASSNAME = 'className'
    CLASS_NAME = 'class_name'
    CLIENTSIDE = 'clientside'  # script namespace
    COLOR = 'color'
    DATA = 'data'
    DISABLED = 'disabled'
    END_DATE = 'end_date'
    HEADER = 'header'
    HREF = 'href'
    ICON = 'icon'
    ID = 'id'
    INDEX = 'index'
    INITIAL_DUPLICATE = 'initial_duplicate'
    INVALID = 'invalid'
    IS_OPEN = 'is_open'
    LABEL = 'label'
    LAST = 'last'
    MAXLENGTH = 'maxlength'
    N_CLICKS = 'n_clicks'
    NUMBER = 'number'
    OPTIONS = 'options'
    ORDER = 'order'
    PAGES_LOCATION = '_pages_location'
    PATHNAME = 'pathname'
    SEARCH='search'
    SIZE = 'size'
    SRC = 'src'
    START_DATE = 'start_date'
    SUBMIT_N_CLICKS = 'submit_n_clicks'
    SUBTYPE = 'subtype'
    TYPE = 'type'
    VALUE = 'value'


class BOOTSTRAP:
    '''Constants specific to Bootstrap
    These are mostly used for coloring or positioning.
    '''
    class ALIGNMENT:
        BOTTOM_END = 'bottom-end'
        CENTER = 'center'
        END = 'end'

    class COLOR:
        DANGER = 'danger'
        DARK = 'dark'
        INFO = 'info'
        LIGHT = 'light'
        PRIMARY = 'primary'
        SECONDARY = 'secondary'
        SUCCESS = 'success'
        TRANSPARENT = 'transparent'
        WARNING = 'warning'
