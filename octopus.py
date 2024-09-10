import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.octopus("hello, " + sys.argv[1])
    