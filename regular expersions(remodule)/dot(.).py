import re

def main():
    str1 = "python \n language pypy ironpython jython lython yar wxyz"
    l = re.findall(r'.',str1)
    print(l)

    l1 = re.findall(r'..',str1)
    print(l1)

    l2 = re.findall(r'.y',str1)
    print(l2)

main()
