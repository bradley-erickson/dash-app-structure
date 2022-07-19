# notes
'''
This file is for creating a requests session so you can securely load in your api key.
We then create a session and add the api key to the header.
Depending on the API you are using, you might need to modify the value `x-api-key`.
'''

# package imports
import os
import requests

# local imports
from .settings import API_KEY

# this is an example API url that produces a fact about a number
api_url = 'http://numbersapi.com'
header_key = {'x-api-key': API_KEY}

# create a session and update the headers
# this API does not require any authentication, so we don't need to update the headers
session = requests.Session()
session.headers.update(header_key)


def get_number_fact(number):
    '''Format the proper url, then call for a fact about the number'''
    url = f'{api_url}/{number}/trivia'
    r = session.get(url)

    # if the response is not 200, then something went wrong and we should return an emtpy string
    if r.status_code != 200:
        return ''
    else:
        return r.content.decode('utf-8')
