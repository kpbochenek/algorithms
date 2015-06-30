import sys
import os
import math
import random

data = sys.argv[1]
program = sys.argv[2]

print('calculating result for ' + data)
print('using program ' + program)

with open(data) as f:
    result = 0
    for phrase in f.readlines():
        command = 'echo "' + phrase[:-1] + '" | ' + program
        #print(command)
        value = os.popen(command).read()
        produced_phrase = os.popen('python validator.py "' + value + '"').read()
        assert phrase == produced_phrase, "phrase:\n|%s|\n not equal to generated \n|%s|\n" % (phrase, produced_phrase)
        result += len(value)
        #print(result)
    print(result)
