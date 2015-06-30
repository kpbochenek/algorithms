First generate random examples issuing command:
python generator.py > gen.in1
python generator.py > gen.in2
python generator.py > gen.in3

Then run automatic testing script with command:
python tester.py gen.in1 "./yourprogram"
python tester.py gen.in2 "./yourprogram"
python tester.py gen.in3 "./yourprogram"

It will for each testcase in provided file execute your program and then run validator on returned output to verify an answer was correct.

simple.py - works on single zone, naive implementation
complex2.py - checks maybe best next move isn't actually best (works 1 move ahead)
complex3.py - calculates best move checking 3 moves ahead - almost reaching time limit

Happy Hacking :)
