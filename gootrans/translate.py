#!/usr/bin/env python2
import urllib
import sys
import json
import re
from key import API_KEY

TRANS_URL = 'https://www.googleapis.com/language/translate/v2?key=%s&source=en&target=fr&q=' % API_KEY
REQ_URL = TRANS_URL + '%s'

clean_regex = re.compile(r'[^\w\s]') # strip none spacing/alphanum

def main():
    trans_data = clean_regex.sub('', sys.argv[1])
    data = urllib.urlopen(REQ_URL % trans_data).read()
    decoded = json.loads(data)
    try:
        translated_text = decoded['data']['translations'][0]['translatedText']
        print '\33[32m%s\33[36m : \33[31m%s\33[0m' % (trans_data, translated_text)
    except IndexError:
        print "*ERROR* Could not translate '%s'" % trans_data

if __name__=='__main__':
    main()
