#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    lst = input('Введите числа через пробел: ')
    tpl = tuple(lst.split())
    ind = 0

    i = 1
    while i < len(tpl):
        if int(tpl[i-1]) == int(tpl[i]) and int(tpl[i]) % 2 == 0:
            ind = i
        i += 1
    i = 0

    while i < ind - 1:
        print(tpl[i])
        i += 1
