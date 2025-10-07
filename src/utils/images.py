# utils/images.py
'''
Read images into the system.
This file reads each file in as bytes then decodes
as a base64 image string to display on a webpage
'''
import base64
import os

import utils.constants as c

_LOGO_PATH = os.path.join(c.PATH.LOGOS, 'logo_main.png')
_LOGO_BYTES = base64.b64encode(open(_LOGO_PATH, 'rb').read())
ENCODED_LOGO = c.DASH.BASE64_IMAGE_STR.format(_LOGO_BYTES.decode())

_LOGO_SMALL_PATH = os.path.join(c.PATH.LOGOS, 'logo_small.png')
_LOGO_SMALL_BYTES = base64.b64encode(open(_LOGO_SMALL_PATH, 'rb').read())
ENCODED_LOGO_SMALL = c.DASH.BASE64_IMAGE_STR.format(_LOGO_SMALL_BYTES.decode())
