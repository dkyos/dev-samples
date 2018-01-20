
import argparse
import sys, os

file = sys.argv[0]
realpath = os.path.realpath(file)
abspath = os.path.abspath(realpath)
#basename = os.path.basename(abspath)
dirname = os.path.dirname(abspath)
sys.path.append(dirname)
dirname = os.path.dirname(dirname)
sys.path.append(dirname)


