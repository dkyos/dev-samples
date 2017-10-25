#!/usr/bin/env python
#-*- coding: utf-8 -*-

# [START skeleton]
"""Skeleton code: Singleton logger and try & except"""

# [START skeleton_import]
import argparse
from sc_header import *
from sc_logger import sc_logger
# [END skeleton_import]

# singleton logger
logger = sc_logger.get_logger()

# [START def_analyze]
def analyze(test_filename):
    """Run test."""

    logger.info("start analyzing...")

    df = pd.DataFrame()
    try:
        df = pd.read_csv(test_filename
            , sep='|'
            , dtype='object'
            , error_bad_lines=False , quoting=csv.QUOTE_NONE
            , encoding='utf-8')
        logger.info("read_csv: %s" % df.shape )
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        logger.error("Error: %s " % e )

    return df
# [END def_analyze]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'test_filename',
        help='The filename of testing you\'d like to analyze.')
    args = parser.parse_args()

    analyze(args.test_filename)
# [END skeleton]
