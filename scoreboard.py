class Scoreboard:
    def __init__(self, filename):
        self.__filename = filename
        self.__scoreboard = {}
        self.Read()
    def GetScoreboard(self):
        return self.__scoreboard
    def Read(self):
        file = open(self.__filename + ".txt")
        content = file.read().split(" ")

        i = 0
        while i < len(content)-1:
            self.__scoreboard[content[i]] = float(content[i+1])
            i += 2

        file.close()

    def Print(self):
        for key in self.__scoreboard:
            print(key + ": + " + str(self.__scoreboard[key]))

    def AddScore(self, name, value):
        self.__scoreboard[name] = float(value)

    def SaveToFile(self):
        file = open(self.__filename + ".txt" , "w")
        for key in self.__scoreboard:
            file.write(key + " " + str(self.__scoreboard[key]) + " ")
        file.close()

S = Scoreboard("number")
S.Print()
S.AddScore("name001", 20.0)
S.AddScore("name002", 27.0)
S.Print()
S.SaveToFile()