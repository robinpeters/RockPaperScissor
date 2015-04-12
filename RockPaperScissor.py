#!/usr/bin/python
#
# Written By    : <RobinPeter@gmail.com>
# Created On    : Fri Apr 10 18:48:24 PDT 2015
# Modified On   : Fri Apr 10 20:24:28 PDT 2015
# Program Name  : RockPaperScissor.py
# Version       : 0.0.1
#
#-------------------------------------------------------------------------------------#
import random
import os
import json
import pprint
#-------------------------------------------------------------------------------------#
def main():
    user, sys = 0, 0
    name = os.getlogin()
    while True:
        dictionary  = {1:'Rock', 2:'Paper', 3:'Scissors'}
        sysChoice   = random.choice(dictionary.keys())
        try:
            userChoice  = int(raw_input("Select One [1:Rock, 2:Paper, 3:Scissors, 0:Exit] : "))
            if (userChoice in (1,2,3)):
                print "Computer Choice is   : ", sysChoice,  dictionary[sysChoice]
                print "Your Choice is       : ", userChoice, dictionary[userChoice]
                result = rockPaperScissors(sysChoice, userChoice)
                print "Result               : ", result
                if (result == 'Win'):
                    user    = user + 1
                    sys     = 0
                    scoreBoard(user, sys, name)
                elif (result == 'Lose'):
                    user    = 0
                    sys     = sys + 1
                    scoreBoard(user, sys, name)
                else:
                    sys, user = 0, 0
                    scoreBoard(user, sys, name)
            elif(userChoice == 0):
                topScore()
                break
            else:
                continue
        except ValueError:
            continue
#-------------------------------------------------------------------------------------#
def rockPaperScissors (a, b):
    if ((a) % 3 + 1 == b):
        return "Win";
    elif ((b) % 3 + 1 == a):
        return "Lose"
    else:
        return "Draw"
#-------------------------------------------------------------------------------------#
def scoreBoard(u, s, name):
    if (os.path.isfile("score.json")): 
        jsonFile = open("score.json", "r")
        data     = json.load(jsonFile)
        jsonFile.close()
        if name in data:
            print "Current Score        : ", u, s
            print "Top Score            : ", data[name]["user"], data[name]["sys"]
            if (u > (data[name]["user"])):
                data[name]["user"] = u
            if (s > (data[name]["sys"])):
                data[name]["sys"] = s
        else:
            data.update({name:{'user':0,'sys':0}})
        jsonFile = open("score.json", "w+")
        json.dump(data, jsonFile, indent=4)
        jsonFile.close()
    else:
        data = {name:{"user":0, "sys":0}}
        jsonFile = open("score.json", "w")
        json.dump(data, jsonFile, indent=4)  
        jsonFile.close()
        os.chmod("score.json", 0666)
#-------------------------------------------------------------------------------------#
def topScore():
    if (os.path.isfile("score.json")):
        jsonFile = open("score.json", "r")
        data     = json.load(jsonFile)
        jsonFile.close()
        dicts = [{k: v} for (k,v) in data.items()]
        dicts.sort(key=lambda d: (d.values()[0]['user'], d.values()[0]['sys'],))
        dicts.reverse()
        print "Top Score : "
        for item in dicts:
            for key in item:
                print '{0:<10} {1:>2} {2:>2}'.format(key, item[key]['user'], item[key]['sys'])
#-------------------------------------------------------------------------------------#
if __name__ == '__main__':main()
#-------------------------------------------------------------------------------------#
# EOF