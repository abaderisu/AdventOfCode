#!/usr/bin/env python3

def parseCard(card):
    card = card.split('|')
    key = [n for n in card[0].split(':')[1].split(' ') if n.isdigit()]
    players = [n for n in card[1].split(' ') if n.isdigit()]

    return len([w for w in players if w in key])

def scoreCards(cards):
    score = 0
    counts = [1 for _ in range(len(cards))]
    for i,c in enumerate(cards):
        winners = parseCard(c)
        if winners > 0:
            score = score + 1 * pow(2, winners - 1)
        
        for j in range(winners):
            counts[i + j + 1] += counts[i]

    return score,sum(counts)

if __name__ == '__main__':
    lines = open('input.txt').read().splitlines()
    score,played = scoreCards(lines)
    print('Part 1',score)
    print('Part 2', played)

