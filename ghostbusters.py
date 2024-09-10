import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.ghostbusters("hello, " + sys.argv[1])
    