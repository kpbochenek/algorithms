from collections import defaultdict

N = int(input())  # Number of elements which make up the association table.
Q = int(input())  # Number Q of file names to be analyzed.
exts = defaultdict(lambda: "UNKNOWN")
for i in range(N):
    EXT, MT = input().split()
    exts['.'+EXT.upper()] = MT

for i in range(Q):
    FNAME = input()  # One file name per line.
    ext = FNAME[FNAME.rfind('.'):]
    print(exts[ext.upper()])
