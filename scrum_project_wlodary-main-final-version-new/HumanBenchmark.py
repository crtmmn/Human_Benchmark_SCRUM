import Histogram
import NumberMemory
import ReactionTime
import Scoreboard
import VerbalMemory
import Player
import os
from colours import bcolors

class HumanBenchmark:
    def __init__(self):
        self.__numberMemory = NumberMemory.NumberMemory()
        self.__reactionTime = ReactionTime.ReactionTime()
        self.__verbalMemory = VerbalMemory.VerbalMemory()
        self.__player = Player.Player()
        self.__scoreboard = Scoreboard.Scoreboard()

    def Play(self):
        playingstopping = 0
        while playingstopping == 0:

            clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            
                
            # self.__player.SetName()    
            # clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            # clearConsole()
            # while True:
            clearConsole()
            print(bcolors.WARNING + "【﻿ＨＵＭＡＮ　ＢＥＮＣＨＭＡＲＫ】" + bcolors.ENDC)
            filename = ""
            choice = input(bcolors.OKCYAN +  "【﻿CHOOSE  THE  GAME: 】" + "\n"  + "【﻿1 - Reaction Time】" + "\n" + "【﻿2 - Verbal memory】" + "\n" +"【﻿3 - Number Memory】" + "\n" + " YOUR  CHOICE: " +  bcolors.ENDC)
            clearConsole()
            if choice == "1":
                filename = "reaction"
                scorechoice = input(bcolors.OKCYAN + "【﻿Do you want see scoreboard or play?: 】" + "\n" + "【﻿1 - Scoreboard】" + "\n" + "【﻿2 - Play game】" + "\n" + bcolors.ENDC)
                clearConsole()
                if scorechoice == "1":
                    print(bcolors.WARNING +"【﻿ＳＣＯＲＥＢＯＡＲＤ】" + bcolors.ENDC)
                    self.__scoreboard.SetFileName(filename)
                    self.__scoreboard.Print()
                    print(bcolors.WARNING +"【﻿ＨＩＳＴＯＧＲＡＭ】" + bcolors.ENDC)

                    H = Histogram.Histogram(self.__scoreboard)
                    H.Print()
                    
                elif scorechoice == "2":
                    self.__player.SetName()
                    self.__reactionTime.Play()
                    self.__player.SetScore(self.__reactionTime.GetScore())

                    decision = input(bcolors.OKCYAN + "【﻿Do you want to save score?】" + "\n" + "【﻿1 - Yes】" + "\n" + "【﻿2 - No】" + "\n" + bcolors.ENDC)

                    if decision == "1":

                        self.__scoreboard.SetFileName(filename)

                        self.__scoreboard.AddScore(self.__player.GetName(), self.__player.GetScore())
                        self.__scoreboard.SaveToFile()
                    elif decision == "2":
                        pass
                    else:
                        print(bcolors.FAIL + "【﻿Enter the correct number】" + bcolors.ENDC)

                else:
                    print(bcolors.FAIL + "【﻿Enter the correct number】" + bcolors.ENDC)

            elif choice == "2":

                filename = "verbal"
                scorechoice = input(bcolors.OKCYAN + "【﻿Do you want see scoreboard or play?: 】" + "\n" + "【﻿1 - Scoreboard】" + "\n" + "【﻿2 - Play game】" + "\n" + bcolors.ENDC)
                clearConsole()
                if scorechoice == "1":
                    print(bcolors.WARNING +"【﻿ＳＣＯＲＥＢＯＡＲＤ】" + bcolors.ENDC)
                    self.__scoreboard.SetFileName(filename)
                    self.__scoreboard.Print()
                    print(bcolors.WARNING +"【﻿ＨＩＳＴＯＧＲＡＭ】" + bcolors.ENDC)

                    H = Histogram.Histogram(self.__scoreboard)
                    H.Print()
                    
                elif scorechoice == "2":
                    self.__player.SetName()
                    self.__verbalMemory.Play()
                    self.__player.SetScore(self.__verbalMemory.GetScore())


                    decision = input(bcolors.OKCYAN + "【﻿Do you want to save score?】" + "\n" + "【﻿1 - Yes】" + "\n" + "【﻿2 - No】" + "\n" + bcolors.ENDC)
                    if decision == "1":

                        self.__scoreboard.SetFileName(filename)

                        self.__scoreboard.AddScore(self.__player.GetName(), self.__player.GetScore())
                        self.__scoreboard.SaveToFile()
                    elif decision == "2":
                        pass
                    else:
                        print(bcolors.FAIL + "【﻿Enter the correct number】" + bcolors.ENDC)

                else:
                    print(bcolors.FAIL + "【﻿Enter the correct number】" + bcolors.ENDC)
            elif choice == "3":
                filename = "number"
                scorechoice = input(bcolors.OKCYAN + "【﻿Do you want see scoreboard or play?: 】" + "\n" + "【﻿1 - Scoreboard】" + "\n" + "【﻿2 - Play game】" + "\n" + bcolors.ENDC)
                clearConsole()
                if scorechoice == "1":
                    print(bcolors.WARNING +"【﻿ＳＣＯＲＥＢＯＡＲＤ】" + bcolors.ENDC)
                    self.__scoreboard.SetFileName(filename)
                    self.__scoreboard.Print()
                    print(bcolors.WARNING +"【﻿ＨＩＳＴＯＧＲＡＭ】" + bcolors.ENDC)

                    H = Histogram.Histogram(self.__scoreboard)
                    H.Print()
                elif scorechoice == "2":
                    self.__player.SetName()
                    self.__numberMemory.Play()
                    self.__player.SetScore(self.__numberMemory.GetScore())

                    decision = input(bcolors.OKCYAN + "【﻿Do you want to save score?】" + "\n" + "【﻿1 - Yes】" + "\n" + "【﻿2 - No】" + "\n" + bcolors.ENDC)
                    if decision == "1":

                        self.__scoreboard.SetFileName(filename)

                        self.__scoreboard.AddScore(self.__player.GetName(), self.__player.GetScore())
                        self.__scoreboard.SaveToFile()
                    elif decision == "2":
                        pass
                    else:
                        print(bcolors.FAIL + "【﻿Enter the correct number】" + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + "【﻿Enter the correct number】" + bcolors.ENDC)

            else:
                print(bcolors.FAIL + "【﻿ENTER  THE  CORRECT  OPTION!】" + bcolors.ENDC)
                quit()

            input(bcolors.OKCYAN + "【﻿Press enter to continue: 】\n" + bcolors.ENDC)
            clearConsole()

            stoppinggame = input(bcolors.OKCYAN + "【﻿do you want to go back to menu】" + "\n" + "1 - Yes" + "\n" + "2 - No" + "\n" + bcolors.ENDC)
            if stoppinggame == "1":
                pass
            elif stoppinggame == "2":
                playingstopping += 1
            else:
                print(bcolors.FAIL + "【﻿ENTER  THE  CORRECT  OPTION!】" + bcolors.ENDC)
                quit()