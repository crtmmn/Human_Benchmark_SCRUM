from Scoreboard import Scoreboard

class Histogram:
    def __init__(self, S):
        self.__S = S
        self.__scores = {}
        self.FillTheScores()

    def FillTheScores(self):
        for key in self.__S.GetScoreboard():
            if self.__S.GetScoreboard()[key] in self.__scores:
                self.__scores[self.__S.GetScoreboard()[key]] += 1
            else:
                self.__scores[self.__S.GetScoreboard()[key]] = 1

    def PrintStars(self, number):
        for i in range(number):
            print("*", end=" ")
        print()

    def Print(self):
        for key in sorted(self.__scores):
            print(str(key) + ": ", end="")
            self.PrintStars(self.__scores[key])

S = Scoreboard("number")

H = Histogram(S)
H.Print()