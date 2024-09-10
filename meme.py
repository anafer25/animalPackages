import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.beavis("hello, " + sys.argv[1])
    