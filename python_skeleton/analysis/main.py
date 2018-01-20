#!/usr/bin/env python
#-*- coding: utf-8 -*-

import argparse
from init import *

from utils.sc_logger import *
from utils.sc_csv import *

# singleton logger
logger = sc_logger.get_logger()

def analyze(filename):
    """Run test."""
    logger.info("start analyzing...")
    df = load_csv_to_df(filename)
    return df

if __name__ == '__main__':
    args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument( "-F", "--filename",
        help='The filename of testing you\'d like to analyze.')

    args = parser.parse_args(args)

    analyze(args.filename)
