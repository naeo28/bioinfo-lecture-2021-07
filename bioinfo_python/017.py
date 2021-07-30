#!/usr/bin/python3

fw = open("write_sample.txt", "w")
fw.write("MEN\n")
fw.close()

# with open으로 파일 열어서 쓰기
with open("write_sample2.txt", "w") as write_handle:
    write_handle.write("BRCA1\n")

# with open으로 파일 열어서 추가하기
with open("write_sample2.txt", "a") as write_handle:
    write_handle.write("BRCA2\n")

def my_function(num):
    """
        input: int
        return: int
        들어오는 숫자에 2를 곱해서 반환
    """
    return num * 2
