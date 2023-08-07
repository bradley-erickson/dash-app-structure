# notes
'''
This file is used for handling anything image related.
I suggest handling the local file encoding/decoding here as well as fetching any external images.
'''

# package imports
import base64
import os

# image CDNs
image_cdn = 'https://images.dog.ceo/breeds'

# logo information
cwd = os.getcwd()
logo_path = os.path.join(cwd, 'assets', 'logos', 'logo_main.png')
logo_tunel = base64.b64encode(open(logo_path, 'rb').read())
logo_encoded = 'data:image/png;base64,{}'.format(logo_tunel.decode())


def get_dog_image(breed, name):
    '''
    This method assumes that you are fetching specific images hosted on a CDN.
    For instance, random dog pics given a breed.
    '''
    if breed and name:
        return f'{image_cdn}/{breed}/{name}.jpg'
    return None
