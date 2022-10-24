import time
import random
import os
import Game
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
class ReactionTime(Game.Game):
    def __init__(self):
        super().__init__()
        self._attempts = 0
        self._scoreboard = []
    def Play(self):
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

        print(bcolors.WARNING + "【﻿ＲＥＡＣＴＩＯＮ　ＴＩＭＥ　ＴＥＳＴ】" + bcolors.ENDC)
        self._attempts = input(bcolors.OKCYAN + " INPUT NUMBER OF ATTEMPS:  " + bcolors.ENDC)

        try:
            int(self._attempts)
            it_is = True
        except ValueError:
            it_is = False
        if it_is == False:
            print(bcolors.FAIL + "Restart the program and enter a integer number" + bcolors.ENDC)
            quit()
        clearConsole()
        i = 0
        while int(self._attempts) > i:
            input(bcolors.OKCYAN + " PRESS   ENTER   TO   START: " + bcolors.ENDC)

            clearConsole()
            
            print(bcolors.FAIL + " WAIT  FOR   GREEN! " + bcolors.ENDC)
            first_point = 0
            rozpoczecie = time.time()
            time_waiting = time.sleep(random.randint(2, 4))
            clearConsole()

            print(bcolors.OKGREEN + " CLICK! " + bcolors.ENDC)
            first_point = time.time()
            
            print(input())

            second_point = time.time()
            result = (second_point - first_point)
            clearConsole()
            if (result * 1000) < 1:
                print(bcolors.FAIL + " TOO EARLY! :  " + bcolors.ENDC)
                quit()
            self._scoreboard.append(result)
            rezzilt = (str(round(result * 1000))+ " ms")
            print(bcolors.OKGREEN + rezzilt + bcolors.ENDC)
            i += 1
            
        for element in self._scoreboard:
            self._score += element
        self._average = self._score / int(self._attempts)
        self._score = round(self._average * 1000)
        print(bcolors.OKGREEN + "Your average is: " + str(self._score) + " ms" + bcolors.ENDC)
        
            
