import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.daemon("hello, " + sys.argv[1])
   