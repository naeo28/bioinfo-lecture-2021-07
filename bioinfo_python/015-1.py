#!/usr/bin/python3

import sys

#s = sys.argv[1]
#s = int(s)
#print(s * 2)

#실습
def make_double(num):
    return num * 2

if len(sys.argv) != 2:    #리스트 길이가 2 안되면, 1도 3도 다 이렇게됨
    print(f"#usage: python {sys.argv[0]} [number]")
    sys.exit()

num = int(sys.argv[1])
result = make_double(num)
print(result)

