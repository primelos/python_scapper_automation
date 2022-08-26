import requests
from bs4 import BeautifulSoup

import re

import sys

print(sys.argv)

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: please enter the TED talk url")

url = 'https://www.ted.com/talks/anicka_yi_art_that_imagines_new_ways_of_living_with_machines'

r = requests.get(url)

print('download about to start', )

soup = BeautifulSoup(r.content, features='lxml')
result = ''
for val in soup.findAll('script'):
    if (re.search('talkPage.init', str(val))) is not None:
        result = str(val)


result_mp4 = re.search('(?P<url>https?://[^\s+)(mp4)', result).group('url')

mp4_url = result_mp4.split('"')[0]
