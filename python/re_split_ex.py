#!/usr/bin/env python

import re

print ("-"*80)
doc = "one, two three.four   five:six"
splitted = re.split(r"[\:\,\.\s]*", doc)
print (splitted)
splitted = re.split(r"([\:\,\.\s]*)", doc)
print (splitted)

print ("-"*80)
doc = "(asdf) AND (asdf)"
splitted = re.split(r"([\(\)])", doc)
print (splitted)

print ("-"*80)
doc = "( (1234 and 134) and asdf OR 1324)~99 AND (asdf) OR ~( asdfasdf )"
splitted = re.split(r"(\)\~\d*)|(\~\()|(\()|(\))", doc)
print (splitted)
splitted = [x.strip() for x in splitted if (x is not None) and (x is not '') and x.strip() is not '']
print (splitted)


