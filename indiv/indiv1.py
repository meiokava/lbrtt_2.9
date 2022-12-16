#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def subs(l):
    if l == []:
        return [[]]
    x = subs(l[1:])
    return x + [[l[0]] + y for y in x]


if __name__ == '__main__':
    z = list(map(int, input().split()))
    print(subs(z))
