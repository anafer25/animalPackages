import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.fox("hello, " + sys.argv[1])
    