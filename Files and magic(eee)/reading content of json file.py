import json
def main():
    f = open("user1.json","r")
    d = json.load(f)
    print(d)
    for key,value in d.items():
        print(key,value)


main()
    
