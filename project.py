#under development

import random
import time

toss = ["heads","tails"]

numbers = [1,2,3,4,5,6]

player_s = []
bot_s    = []

target = []


time.sleep(1)
print("rules".upper())
print("this is two overs match - 12 balls only".upper())
time.sleep(0.6)

print("this is only one wicket match".upper())
time.sleep(0.6)

print("eligible numbers are from '1 - 6' - 'ONE - SIX'".upper())
time.sleep(0.6)


player = str(input("choose heads/tails : "))
if(player == "heads"):
    time.sleep(1)
    print("bot is tails")
if(player == "tails"):
    time.sleep(1)
    print("bot is heads")
    
decision = random.choice(toss)

time.sleep(0.75)

print("the toss randomly choosen is : ",decision)

if(player==decision):

    print(f"player won the toss {decision}")
    time.sleep(0.3)
    playplayer = str(input("choose bat or bowl : "))
    time.sleep(0.3)
    print(f"player won the toss and choose to {playplayer} first")

    if(playplayer=="bat"):

        for i in range(1,7,1):
            run = int(input("enter the run : "))
            if(run>0 and run<=6):
                bot = random.choice(numbers)
                print("the ball is : ",bot)
                if(run!=bot):
                    player_s.append(run)
                    if(i == 6):
                       print("the player final score is : ",sum(player_s))
                       target = sum(player_s)+1
                       time.sleep(1)
                       print(f"the bot need {target} runs to win the match".upper())
                else:
                    print("the player final score is : ",sum(player_s))
                    target = sum(player_s)+1
                    time.sleep(1)
                    print(f"the bot need {target} runs to win the match".upper())
                    break
            else:
                print("that ball will be calculated and run not be added, no re-ball")

        


    if(playplayer=="bowl"):

        for i in range(1,7,1):
            ball = int(input("enter to bowl : "))
            if(ball>0 and ball<=6):
                run = random.choice(numbers)
                print("the run is : ",run)
                if(ball!=run):
                    bot_s.append(run)
                    if(i == 6):
                       print("the bot final score is : ",sum(bot_s))
                       target = sum(bot_s)+1
                       time.sleep(1)
                       print(f"the player need {target} runs to win the match".upper())
                else:
                    print("the bot final score is : ",sum(bot_s))
                    target = sum(bot_s)+1
                    time.sleep(1)
                    print(f"the player need {target} runs to win the match".upper())
                    break
            else:
                print("that ball will be calculated and run not be added, no re-ball")

else:

    print(f"bot won the toss {decision}")
    time.sleep(0.3)
    playbot = random.choice(["bat","bowl"])
    time.sleep(0.3)
    print(f"bot won the toss and choose to {playbot} first")

    if(playbot == "bat"):

        for i in range(1,7,1):
            ball = int(input("enter to bowl : "))
            if(ball>0 and ball<=6):
                run = random.choice(numbers)
                print("the run is : ",run)
                if(ball!=run):
                    bot_s.append(run)
                    if(i == 6):
                       print("the bot final score is : ",sum(bot_s))
                       target = sum(bot_s)+1
                       time.sleep(1)
                       print(f"the player need {target} runs to win the match".upper())
                else:
                    print("the bot final score is : ",sum(bot_s))
                    target = sum(bot_s)+1
                    time.sleep(1)
                    print(f"the player need {target} runs to win the match".upper())
                    break
            else:
                print("that ball will be calculated and run not be added, no re-ball")

    if(playbot == "bowl"):
        for i in range(1,7,1):
            run = int(input("enter the run : "))
            if(run>0 and run<=6):
                ball = random.choice(numbers)
                print("the ball is : ",ball)
                if(ball!=run):
                    player_s.append(run)
                    if(i == 6):
                       print("the player final score is : ",sum(player_s))
                       target = sum(player_s)+1
                       time.sleep(1)
                       print(f"the bot need {target} runs to win the match".upper())
                else:
                    print("the player final score is : ",sum(player_s))
                    target = sum(player_s)+1
                    time.sleep(1)
                    print(f"the bot need {target} runs to win the match".upper())
                    break
            else:
                print("that ball will be calculated and run not be added, no re-ball")




        

        

















