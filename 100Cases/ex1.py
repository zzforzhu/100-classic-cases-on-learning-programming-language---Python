#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: ex1.py

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a != b) and (b != c) and (c != a):
                num = 100 * a + 10 * b + c
                print num
                    
