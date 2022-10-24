import Histogram
import NumberMemory
import ReactionTime
import Scoreboard
import VerbalMemory
import Player
import os

class HumanBenchmark:
    def __init__(self):
        self.__numberMemory = NumberMemory.NumberMemory()
        self.__reactionTime = ReactionTime.ReactionTime()
        self.__verbalMemory = VerbalMemory.VerbalMemory()
        self.__player = Player.Player()
        self.__scoreboard = Scoreboard.Scoreboard()

    def Play(self):
        class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKCYAN = '\033[96m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            
        print(bcolors.WARNING + "【﻿ＨＵＭＡＮ　ＢＥＮＣＨＭＡＲＫ】" + bcolors.ENDC)
        self.__player.SetName()    
        
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

        print(bcolors.WARNING + "【﻿ＨＵＭＡＮ　ＢＥＮＣＨＭＡＲＫ】" + bcolors.ENDC)
        filename = ""
        choice = input(bcolors.OKCYAN +  "【﻿CHOOSE   THE   GAME : 】" + "\n"  + "【﻿1 - Reaction Time】" + "\n" + "【﻿2 - Verbal memory】" + "\n" +"【﻿3 - Number Memory】" + "\n" + " YOUR  CHOICE: " +  bcolors.ENDC)
        if choice == "1":
            filename = "reaction"
            self.__reactionTime.Play()
            self.__player.SetScore(self.__reactionTime.GetScore())
        elif choice == "2":
            filename = "verbal"
            self.__verbalMemory.Play()
            self.__player.SetScore(self.__verbalMemory.GetScore())
        elif choice == "3":
            filename = "number"
            self.__numberMemory.Play()
            self.__player.SetScore(self.__numberMemory.GetScore())
        else:
            print(bcolors.FAIL + "【﻿ENTER  THE  CORRECT  OPTION!】" + bcolors.ENDC)
            quit()
        
        self.__scoreboard.SetFileName(filename)
        self.__scoreboard.AddScore(self.__player.GetName(), self.__player.GetScore())
        self.__scoreboard.Print()
        self.__scoreboard.SaveToFile()
        H = Histogram.Histogram(self.__scoreboard)
        H.Print()

        
        
        
    
