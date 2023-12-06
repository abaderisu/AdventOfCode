#!/usr/bin/env python3

def parseCal(s,useStrings):
    firstI = len(s)
    firstV = 0
    secondI = -1 
    secondV = 0
    keys = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    if useStrings:
        keys.update({'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,
                     'seven':7,'eight':8,'nine':9,'zero':0})
    for k,v in keys.items():
        idx = s.find(k)
        if idx == -1:
            continue

        if idx < firstI:
            firstV = v
            firstI = idx

        idx = s.rfind(k)
        if idx > secondI:
            secondV = v
            secondI = idx
    return firstV * 10 + secondV

def parseCalDoc(lines,useStrings):
    return sum([parseCal(l,useStrings) for l in lines])

if __name__ == '__main__':
    lines = open('input.txt').readlines()
    print('Part 1',parseCalDoc(lines,False))
    print('Part 2',parseCalDoc(lines,True))
