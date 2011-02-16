#!/usr/bin/env python2
import urllib
import sys
import json
from key import API_KEY

TRANS_URL = 'https://www.googleapis.com/language/translate/v2?key=%s&source=en&target=fr&q=' % API_KEY
REQ_URL = TRANS_URL + '%s'

def main():
    data = urllib.urlopen(REQ_URL % sys.argv[1]).read()
    decoded = json.loads(data)
    try:
        print decoded['data']['translations'][0]['translatedText']
    except IndexError:
        print "*ERROR* Could not translate"

if __name__=='__main__':
    main()
