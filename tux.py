import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.tux("hello, " + sys.argv[1])
    