import sys
import math
import random

tests = 100

def generate_letter():
    letter = chr(random.randint(ord('@'), ord('Z')))
    return letter.replace('@', ' ')
    

def generate():
    return "".join([generate_letter() for x in range(random.randint(10, 500))])

for i in range(tests):
    print(generate())
    
