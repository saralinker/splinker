#!/usr/bin/env python
import sys
import re

inf = sys.argv[1]
of = sys.argv[2]

ih = open(inf,'r')
oh = open(of,'w')

try:
    readcount = 0
    length = 220
    carat = re.compile('>')
    A = {}
    T = {}
    C = {}
    G = {}
    for it in range(1,220):
        A[it] = 0
        C[it] = 0
        G[it] = 0
        T[it] = 0
    for line in ih:
        line.strip
        if carat.search(line):
            count = 0
            readcount += 1
        else:
            for i in line:
                count += 1
                if (i == "A"):
                    tmp = A[count]
                    tmp +=1
                    A[count] = tmp
                elif (i == "C"):
                    tmp = C[count]
                    tmp +=1
                    C[count] = tmp
                elif (i == "G"):
                    tmp = G[count]
                    tmp +=1
                    G[count] = tmp
                else:
                    tmp = G[count]
                    tmp +=1
                    G[count] = tmp
                
finally:
    for it in range(1,length):
        ATtmp = ((A[it] + T[it]) * 1.0) / readcount
        GCtmp = ((C[it] + G[it]) * 1.0) / readcount
        tmpit = str(it)
        ATtmp = str(ATtmp)
        GCtmp = str(GCtmp)
        oh.write(tmpit + "\t" + ATtmp + "\t" + GCtmp + "\n")
        
    ih.close
    oh.close

