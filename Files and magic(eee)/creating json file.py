import json

def main():
    f = open("user1.json","w")
    user = {"name":"giri",
            "uname":"nit",
            "password":"nit123"}
    json.dump(user,f)
    f.close()

main()
