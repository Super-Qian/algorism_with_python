#!/usr/bin/env python
# coding=utf-8
def fibo(n):
    if n < 3:
        return 1
    a = fibo(n-2) + fibo(n-1)
    return a

print fibo(8)
