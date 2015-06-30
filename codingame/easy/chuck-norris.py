import sys, math
import binascii
import itertools

v = lambda x: '0 ' if (x == '1') else '00 '

MESSAGE = input()

value = ''.join([bin(int.from_bytes(c.encode(), 'big'))[2:].lstrip('0').zfill(7) for c in MESSAGE])

print(''.join([v(k) + '0'*len(list(g)) + ' ' for k, g in itertools.groupby(value)]).strip())
