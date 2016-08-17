#! /usr/bin/env python

import HTMLParser
from MLStripper import strip_tags
import fileinput
import json
import pprint
import random
import re
import sys
import string

random.seed (8675309)
shufbufsize = 1000000

mode = sys.argv.pop ()
assert (mode == 'train' or mode == 'test' or mode == 'valid')

parse = HTMLParser.HTMLParser ()

def preprocess (what):
    return parse.unescape (strip_tags (re.sub('^\s+', '', re.sub ('\s+', ' ', what))))

reload (sys)
sys.setdefaultencoding ('utf-8')

shufbuf=[None for x in xrange(shufbufsize)]

pp = pprint.PrettyPrinter ()
problem = None
lastguid = None

for line in fileinput.input():
    fields = string.split (line, '\t')
    guid = fields[0]
    if mode == 'train':
        if guid.endswith ('0') or    \
           guid.endswith ('1'):
          continue
    elif mode == 'valid':
        if not guid.endswith ('0'):
          continue
    elif mode == 'test':
        if not guid.endswith ('1'):
          continue
    else:
        assert False

    seqno = fields[1]
    whom = fields[2]
    utterance = preprocess (fields[3])
    labels = json.loads (fields[4])

    if lastguid != guid:
        problem = None
        lastguid = guid

    if problem == None:
        if whom == 'USER' and                   \
           len (labels) > 0 and                 \
           labels[0]['Label'] == 'PRBLM':
            problem = utterance
    else:
        if whom == 'AGENT':
            index = random.randint (0, shufbufsize-1)
            if shufbuf[index] != None:
                [problem2, utterance2] = shufbuf[index]
                if problem != problem2:
                    print '\t'.join ([problem, utterance, utterance2])
                    print '\t'.join ([problem2, utterance2, utterance])
            shufbuf[index] = [problem, utterance]

problem = None

for index in xrange(shufbufsize):
    if shufbuf[index] != None:
        if problem != None:
            [problem2, utterance2] = shufbuf[index]
            if problem != problem2:
                print '\t'.join ([problem, utterance, utterance2])
                print '\t'.join ([problem2, utterance2, utterance])
            problem = None
        else:
            [problem, utterance] = shufbuf[index]

