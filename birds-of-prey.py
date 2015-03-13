# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 11:06:11 2015

@author: nfette
"""
import string
import itertools
from collections import deque

# Key: (C)ondor (E)agle (K)estrel (O)wl; (H)eads (T)ails
cards = map(string.split,
            """KT OH EH CH
            OH KH CT CH
            OT ET CH KH
            ET OT KH CH
            CH KH OH ET
            EH KH OT CT
            EH OH KT CT
            EH KH ET CH
            KT OT OH ET""".split('\n'))

edges = [(0,0,1,2),
         (0,1,3,3),
         (1,0,2,2),
         (1,1,4,3),
         (2,1,5,3),
         (3,0,4,2),
         (3,1,6,3),
         (4,0,5,2),
         (4,1,7,3),
         (5,1,8,3),
         (6,0,7,2),
         (7,0,8,2)]

edgesByCard = []
for card in range(9):
    edgesOfCard = [(i,j,k,l) for (i,j,k,l) in edges if card == k and card > i]
    edgesByCard.append(edgesOfCard)

def match(a,b):
    return a[0] == b[0] and a[1] != b[1]

def isValid2(seq, rotseq):
    for edgesOfCard in edgesByCard[:len(seq)]:
        for (i,j,k,l) in edgesOfCard:
            if not match(cards[seq[i]][(j+rotseq[i])%4],
                     cards[seq[k]][(l+rotseq[k])%4]):
                return k
    return 0

tries = 0
threes = []
for seq in itertools.permutations(range(9),3):
    for rotseq in itertools.product(range(4), repeat=len(seq)):
        a = isValid2(seq, rotseq)
        tries += 1
        if not a:
            threes.append((seq,rotseq))        
print "{} tries, {} sequences of three cards".format(tries,len(threes))
sixes = []
for seq1,rotseq1 in threes:
    for seq2, rotseq2 in threes:
        seq = seq1 + seq2
        if len(set(seq)) != 6:
            continue
        rotseq = rotseq1 + rotseq2
        a = isValid2(seq, rotseq)
        tries += 1
        if not a:
            sixes.append((seq, rotseq))
print "{} tries, {} sequences of six cards".format(tries,len(sixes))
nines = []
for seq1,rotseq1 in sixes:
    for seq2, rotseq2 in threes:
        seq = seq1 + seq2
        if len(set(seq)) != 9:
            continue
        rotseq = rotseq1 + rotseq2
        a = isValid2(seq, rotseq)
        tries += 1
        if not a:
            nines.append((seq, rotseq))
print "{} tries, {} sequences of nine cards".format(tries,len(nines))

# 32256 tries, 528 sequences of three cards
# 96192 tries, 228 sequences of six cards
# 97348 tries, 4 sequences of nine cards

for card, rotcard in zip(*nines[0]):
    d = deque(cards[card])
    d.rotate(rotcard)
    print card, rotcard, d
