from scoreboard import Scoreboard

class Histogram:
    def _init__(self, S):
        self.__S = S
        self.__scores = {}
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
        i = 0
        self.PrintStars(10)


S = Scoreboard("number")
S.Print()
S.AddScore("name001", 20.0)
S.AddScore("name002", 27.0)
S.Print()
S.SaveToFile()

H = Histogram(5)
H.Print()