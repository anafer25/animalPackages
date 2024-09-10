import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.cheese("hello, " + sys.argv[1])
   