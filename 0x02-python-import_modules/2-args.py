#!/usr/bin/python3
import sys
counter = len(sys.argv) - 1
if counter == 0:
    print("0 arguments.")
elif counter == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(counter))
for i in range(1, counter + 1):
    print("{:d}: {:s}".format(i, sys.argv[i]))
