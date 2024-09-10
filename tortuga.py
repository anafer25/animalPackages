import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.turtle("hello, " + sys.argv[1])
    