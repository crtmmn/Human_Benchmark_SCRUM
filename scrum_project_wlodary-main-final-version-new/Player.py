from colours import bcolors
class Player:
    def __init__(self):
        self.__name = ""
        self.__score = 0
    def GetName(self):
        return self.__name
    def GetScore(self):
        return self.__score
    def SetName(self):
        self.__name = input(bcolors.OKCYAN +"Enter name: " + bcolors.ENDC)
    def SetScore(self, score):
        self.__score = score