
import string
import random

def urlGen(urlLen = 12, letters = string.ascii_letters):
    return ''.join(random.choice(letters) for i in range(urlLen))