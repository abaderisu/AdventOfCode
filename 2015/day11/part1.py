#!/usr/bin/env python3

def increment_password(password):
    change = lambda string, index, char : string[:index] + char + string[index + 1:]

    i = len(password) - 1
    while i >= 0:
        c = password[i]
        if c == 'z':
            password = change(password, i, 'a')
            i -= 1
        else:
            password = change(password, i, chr(ord(c) + 1))
            break

    return password

def validate(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    run = False
    for i in range(0, len(password) - 2):
        first = ord(password[i])
        second = ord(password[i + 1])
        third = ord(password[i + 2])
        if second - first == 1 and third - second == 1:
            run = True
            break

    pair = ('',-10)
    double = False
    for i in range(0, len(password) - 1):
        w = password[i] + password[i + 1]
        if w[0] == w[1]:
            if pair[0] == '':
                pair = (w, i)
            elif i != (pair[1] + 1):
                double = True
                break
    return run and double

password = 'vzbxkghb'
while True:
    password = increment_password(password)
    if validate(password):
        print(password)
        break
