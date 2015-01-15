#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # python 3
    from urllib import request
    from urllib.parse import urlencode
except ImportError:
    # python 2
    import urllib2 as request
    from urllib import urlencode

import json    
    

API_KEY = 'INSERT_API_KEY_HERE'

# the language used in any status/error messages by the API. Can be 'en' or 'cy'
API_LANG = 'cy'

API_URL = 'http://api.techiaith.org/pos/v1/?'

def get_from_api(text):
    params = {
        'text' : text.encode('utf-8'),
        'api_key' : API_KEY.encode('utf-8'),
        'lang' : API_LANG.encode('utf-8')
    }
    
    url = API_URL + urlencode(params)
    
    response = request.urlopen(url)
    response = json.loads(response.read())
    if not response['success']:
        # Gwall gyda'r galwad API
        error_messages = u'\n'.join(response['errors'])
        raise ValueError(error_messages)
    
    return response['result']
    
    

def tag_text(text):
    tagged_text = get_from_api(text)
    for tagged_word in tagged_text.split(" "):
        word, pos, mutation = tagged_word.split("/")
        if mutation == "-":
            mutation = None
        elif mutation is "?":
            mutation = "Unknown"
        print("WORD: {}\nPOS: {}\nMUTATION: {}\n-----------".format(word, pos, mutation))


if __name__ == "__main__":
    tag_text(u"mae hen wlad fy nhadau")