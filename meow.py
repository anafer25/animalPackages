import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.meow("hello, " + sys.argv[1])
