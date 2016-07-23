#!/usr/bin/env python3
import math

big = 0.3010299


def Icalc(pos, neg):
    total = float(pos + neg)
    return -1*(pos/total)*math.log(pos/total,2) - (neg/total)*math.log(neg/total, 2)


bigtotal = 12.0
pos1 = 3
neg1 = 1
total1 = float(pos1+neg1)

pos2 = 1
neg2 = 2
total2 = float(pos2+neg2)

pos3 = 2
neg3 = 3
total3 = float(pos3 + neg3)

print(Icalc(6,6))

ans = Icalc(6,6) - ((total1/bigtotal)*Icalc(pos1, neg1) + total2/bigtotal*(Icalc(pos2,
    neg2)) + total3/bigtotal*(Icalc(pos3, neg3)))

print(ans)
