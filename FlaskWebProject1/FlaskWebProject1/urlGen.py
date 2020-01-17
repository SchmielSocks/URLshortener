
import string
import random

def urlGen(url, custom, urlLen = 12, letters = string.ascii_letters):
    site = 'http://urlshortener.com/'
    if custom == '':
        return site + ''.join(random.choice(letters) for i in range(urlLen))
    else:
        return site + custom
