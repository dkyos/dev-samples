#!/usr/bin/env python

import pandas as pd
import io
import timeit
from datetime import datetime

DATE_FORMATS = ["%m/%d/%Y","%Y/%m/%d"]

def dateparse(x):
    my_date = None
    for date_format in DATE_FORMATS:
        try:
            my_date = datetime.strptime(x, date_format)
        except ValueError:
            pass
        else:
            break
    return my_date

print ("= Read csv ===================================")
df = pd.read_csv("multi_date_format.csv"
    , delimiter=r"|")
print (df)

print ("\n= Read csv with parse multiple date format  ==")
print ("= Formats : [{}, {}]  ==".format(DATE_FORMATS[0], DATE_FORMATS[1]))
df = pd.read_csv("multi_date_format.csv"
    , delimiter=r"|"
    , parse_dates=['Date']
    , date_parser=dateparse)
print (df)


t="""Num|Date|X1|X2
1|12/6/2017|928.88|3.19
2|1/6/2018|928.86|3.37
4|3/6/2012|930.26|3.38
7|2016/05/04|930.37|3.41
10|2017/1/2|930.39|3.49
00|2012/3/5|930.15|3.54
12|2014/12/12|930.36|3.46"""

iteration = 5000

print ("\n= Iteration {} : Read csv ============".format(iteration))
def test_parse(printout=False):
    df = pd.read_csv(io.StringIO(t)
        , delimiter=r"|")
print(timeit.timeit(test_parse, number=iteration))

print ("\n= Iteration {} : Read csv with parse multiple date format ==".format(iteration))
def test_parse(printout=False):
    df = pd.read_csv(io.StringIO(t)
        , delimiter=r"|"
        , parse_dates=['Date']
        , date_parser=dateparse)
print(timeit.timeit(test_parse, number=iteration))






