
import string as String
import random as Rand

def urlGen(urlLen = 12):
    letters = String.ascii_letters
    return = ''.join(Rand.choice(letters) for i in range(urlLen))

print(urlGen())