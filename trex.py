import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
    # transcript: python trex.py 'name'