#!/usr/bin/env python
#-*- coding: utf-8 -*-

import argparse

from general_utils import *
from config import *

config = Config()
logger = config.logger

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

    if args.filename is None:
        filename = config.filename
    else:
        filename = args.filename

    analyze(filename)
