#!/usr/bin/env python
import random
import itertools
import re
import numpy as np
import math

from shanepy import *

# Total number of clues is cnt_rows*cnt_cols.
# Total number of marked words is cnt_agents.
cnt_rows = 5
cnt_cols = 5
cnt_agents = 8

# Agressiveness in [0, infinity).
# Higher means more agressive.
agg = .5

# This file stores the "solutions" the bot had intended,
# when you play as agent and the bot as spymaster.
log_file = open('log_file', 'w')


print('...Loading vectors')
vectors = np.load('dataset/glove.6B.300d.npy')
print('...Loading words')
word_list = [w.lower().strip() for w in open('dataset/words')]
print('...Making word to index dict')
word_to_index = {w:i for i,w in enumerate(word_list)}
print('...Loading codenames')
codenames = [w.lower().strip().replace(' ','-') for w in open('wordlist2')]
codenames = [w for w in codenames if w in word_to_index]
print('Ready!')


def word_to_vector(word):
    return vectors[word_to_index[word]]

def main():
    import sys
    try:
        with open("/var/smulliga/source/git/mullikine/codenames/sentence.txt", "r") as infile:
            lines = infile.readlines()[0]
            lines = b("sed 's/[,.;]/ & /g' | sed 's/ \+/ /g'", lines)
            # lines = b("escape-11.05.19.sh", lines)
            line = lines[0].lower()

            lwvec = []
            for w in line.split(" "):
                try:
                    lwvec.append(list(word_to_vector(w)))
                    # print(np.array(lwvec).shape)
                except Exception:
                    print(w)

            # lwvec.append(np.zeros((1,300)))

    except IOError:
        print >> sys.stderr, "Some I/O Error occurred"
        sys.exit(1)


    word_to_vector("hand")
    from ptpython.repl import embed
    embed(globals(), locals())

main()