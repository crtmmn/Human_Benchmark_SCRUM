from decimal import InvalidOperation
import random
import Game
import os
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
class VerbalMemory(Game.Game):
    def __init__(self):
        super().__init__()
        self._words =  ["idea", "fowl", "fact", "lift", "crate", "club", "reading", "limit", "shape", "border"]
        self._used_words = []
        self._lives = 3
        self._points = 0
    def Play(self):
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
                    self._points += 1
                    print(bcolors.OKGREEN+"Now you have " + str(self._points) + " points!"+bcolors.ENDC)
            elif user_choice == "2":
                
                if random_choice in self._used_words:
                    clearConsole()
                    print(bcolors.OKGREEN + "CORRECT!" + bcolors.ENDC)

                    self._points += 1
                    print(bcolors.OKGREEN+"Now you have " + str(self._points) + " points!"+bcolors.ENDC)
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
            print(bcolors.OKGREEN + "You had " + str(self._points) + " points" + bcolors.ENDC)
                
            
VM = VerbalMemory()
VM.Play()