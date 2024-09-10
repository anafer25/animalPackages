import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.kitty("hello, " + sys.argv[1])
    