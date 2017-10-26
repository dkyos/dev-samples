#!/usr/bin/env python
#-*- coding: utf-8 -*-

# [START skeleton]
"""Skeleton code: Singleton logger and try & except"""

# [START skeleton_import]
import argparse
from sc_header import *
from sc_logger import sc_logger
from sc_csv import *
# [END skeleton_import]

# singleton logger
logger = sc_logger.get_logger()

# [START def_analyze]
def analyze(filename):
    """Run test."""
    logger.info("start analyzing...")
    df = load_csv_to_df(filename)
    return df
# [END def_analyze]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'filename',
        help='The filename of testing you\'d like to analyze.')
    args = parser.parse_args()

    analyze(args.filename)
# [END skeleton]
