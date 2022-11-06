from decimal import InvalidOperation
import random
import Game
import os
from colours import bcolors

class VerbalMemory(Game.Game):
    def __init__(self):
        super().__init__()
        self._words =  ["idea", "fowl", "fact", "lift", "crate", "club", "reading", "limit", "shape", "border", "soup", "sand", "oil", "butterfly", "forest", "wood", "log", "roof", "gift"]
        self._used_words = []
    def Play(self):
        self._score = 0
        self._lives = 3
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print(bcolors.WARNING + "【﻿ＶＥＲＢＡＬ　　ＭＥＭＯＲＹ】" + bcolors.ENDC)
        while self._lives > 0:
            random_choice = random.choice(self._words)
            print(bcolors.OKCYAN + random_choice + bcolors.ENDC)
            print(" ")
            print(bcolors.OKCYAN +"1 - NEW" + "\n" + "2 - SEEN" + bcolors.ENDC)
            user_choice = input()
            try:
                int(user_choice)
                it_is = True
            except ValueError:
                it_is = False
            if it_is == False:
                print(bcolors.FAIL + "Restart the program and enter a number" + bcolors.ENDC)
                quit()
                
            if user_choice == "1":    
                if random_choice in self._used_words:
                    self._lives -= 1
                    clearConsole()
                    print(bcolors.FAIL + "WRONG!" + bcolors.ENDC)
                    print(bcolors.FAIL + "Now you have " + str(self._lives) + " lives!" + bcolors.ENDC)
                else:
                    clearConsole()
                    print(bcolors.OKGREEN + "CORRECT!" + bcolors.ENDC)
                    self._used_words.append(random_choice)
                    self._score += 1
                    print(bcolors.OKGREEN+"Now you have " + str(self._score) + " points!"+bcolors.ENDC)
            elif user_choice == "2":
                
                if random_choice in self._used_words:
                    clearConsole()
                    print(bcolors.OKGREEN + "CORRECT!" + bcolors.ENDC)

                    self._score += 1
                    print(bcolors.OKGREEN+"Now you have " + str(self._score) + " points!"+bcolors.ENDC)
                else:
                    clearConsole()
                    self._lives -= 1
                    print(bcolors.FAIL + "WRONG!" + bcolors.ENDC)
                    print(bcolors.FAIL+"Now you have " + str(self._lives) + " lives!"+bcolors.ENDC)
            else:
                clearConsole()
                print(bcolors.FAIL+"Restart the program and enter a correct number!"+bcolors.ENDC)
                quit()
        if self._lives == 0:
            clearConsole()
            print(bcolors.FAIL + "YOU LOSE" + bcolors.ENDC)
            print(bcolors.OKGREEN + "You had " + str(self._score) + " points" + bcolors.ENDC)
                
            