import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.milk("hello, " + sys.argv[1])
    