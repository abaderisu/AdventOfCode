#!/usr/bin/env python3

def parse_tree(input):
    tree = []
    for line in input:
        tree.append([int(c) for c in line])
    return tree

def is_visible(i,j,tree):
    height = tree[i][j]
    gridlen = len(tree)

    up = i - 1
    while up >= 0 and tree[up][j] < height:
        up -= 1
    if up < 0:
        return True

    down = i + 1
    while down < gridlen and tree[down][j] < height:
        down += 1
    if down == gridlen:
        return True

    left = j - 1
    while left >= 0 and tree[i][left] < height:
        left -= 1
    if left < 0:
        return True

    right = j + 1
    while right < gridlen and tree[i][right] < height:
        right += 1
    return right == gridlen

def num_visible(tree):
    gridlen = len(tree)
    visible = 0
    for i in range(1,gridlen-1):
        for j in range(1,gridlen-1):
            if is_visible(i,j,tree):
                visible += 1

    # middle visible + edge of grid
    return visible + gridlen * 4 - 4

def scenic_score(i,j,tree):
    height = tree[i][j]
    gridlen = len(tree)

    up = i - 1
    while up > 0 and tree[up][j] < height:
        up -= 1

    down = i + 1
    while down < gridlen - 1 and tree[down][j] < height:
        down += 1

    left = j - 1
    while left > 0 and tree[i][left] < height:
        left -= 1

    right = j + 1
    while right < gridlen - 1 and tree[i][right] < height:
        right += 1

    return (i-up)*(down-i)*(j-left)*(right-j)

def highest_score(tree):
    scores = []
    gridlen=len(tree)
    for i in range(1,gridlen-1):
        for j in range(1,gridlen-1):
            scores.append(scenic_score(i,j,tree))

    return max(scores)

if __name__ == '__main__':
    tree = parse_tree([line.strip() for line in open('input.txt').readlines()])
    print('Part 1',num_visible(tree))

    print('Part 2',highest_score(tree))
