import re
# import pdb;
breakpoint()
def main():
    # pdb.set_trace()
    name = input('enter name')
    m = re.fullmatch(r'[a-z]+',name)
    if m!=None:
        print(f'{name} is vallid')
    else:
        print(f'{name} is not vallid')

main()
