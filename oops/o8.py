class Player:
    def __init__(self):
        self.__name = None
        self.__score = None
    def readplayer(self):
        self.name = input("enter name")
        self.score = int(input("enter score"))
    def printplayer(self):
        print(f'{self.name}\t{self.score}')
def main():
    n = int(input("enter how many players?"))
    playerList = []
    for i in range(n):
        p = Player()
        p.readplayer()
        playerList.append(p)

    for p in playerList:
        p.printplayer()


main()
