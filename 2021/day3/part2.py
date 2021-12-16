#!/usr/bin/env python3

def oxygen_filter(e,i,total):
    if total[1] >= total[0]:
        return e[i] == '1'
    else:
        return e[i] == '0'

def co2_filter(e,i,total):
    if total[1] >= total[0]:
        return e[i] == '0'
    else:
        return e[i] == '1'

def bit_criteria(diagnostics,predicate):
    for i in range(0,len(diagnostics[0])):
        total = [0,0]
        total[0] = sum(1 for e in diagnostics if e[i] == '0')
        total[1] = sum(1 for e in diagnostics if e[i] == '1')

        diagnostics = [e for e in diagnostics if predicate(e,i,total)]
        if len(diagnostics) == 1:
            break

    return int(diagnostics[0],2)

oxygen = [line.strip() for line in open('input.txt')]
co2 = oxygen

oxygen = bit_criteria(oxygen, oxygen_filter)
co2 = bit_criteria(co2, co2_filter)

print(oxygen*co2)
