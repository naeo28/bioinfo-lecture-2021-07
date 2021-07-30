#!/usr/bin/python3

import sys

#num1 = 3
num1 = int(sys.argv[1]) #.py 로 실행할 때 뒤에 숫자 붙힘 그럼 "3" -> 3

if num1 % 2 == 0:
    print("짝수")
else:
    print("홀수")

