#!/usr/bin/env python

import pandas as pd
import re
import timeit

########################################################################
miscdict = {" isn't ": ' is not '," aren't ":' are not '," wasn't ":' was not '," snevada ":' Sierra Nevada '}
miscdict_comp = {re.compile(k): v for k, v in miscdict.items()}

data = pd.DataFrame(
    {
        "id":["HHP","HHP","HHP", "HHP"],
        "type":["General", "General", "General", "General"],
        "channel":["Telephone", "Telephone", "Telephone","Telephone"],
        "Comment":["beer isn't ok","beer isn't ok","beer wasn't available"," snevada is good"]
    }
)

print("======== precomplied sub ============")
def alt3(printout=False):
    def parse_text(text):
        for pattern, replacement in miscdict_comp.items():
            text = pattern.sub(replacement, text)
        return text
    data['Comment_modify'] = data['Comment'].apply(parse_text)
    if printout:
        print(data)

#alt3(printout=True)
#print(timeit.timeit(alt3, number=10000))

print("======== precomplied sub ============")
def alt3(printout=False):
    def parse_text(id, type, chnnel, text):
        for pattern, replacement in miscdict_comp.items():
            text = pattern.sub(replacement, text)
        return text
    data['Comment_modify'] = data.apply(lambda x: parse_text(x['id'], x['type'], x['channel'], x['Comment']), axis=1)
    if printout:
        print(data)
alt3(printout=True)
print(timeit.timeit(alt3, number=100000))

print("======== precomplied sub ============")
def alt4(printout=False):
    def parse_text(text):
        for pattern, replacement in miscdict_comp.items():
            text = pattern.sub(replacement, text)
        return text
    data['Comment_modify'] = data['Comment'].apply(parse_text)
    if printout:
        print(data)

data = data[(data['id'] == 'HHP') & (data['type'] == 'General') & (data['channel'] == 'Telephone')]
alt4(printout=True)
print(timeit.timeit(alt4, number=100000))

########################################################################
