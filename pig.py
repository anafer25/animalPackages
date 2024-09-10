import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.pig("hello, " + sys.argv[1])
    