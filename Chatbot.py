import random

command_1  = ["hello eva", "eva", "wake up eva", "you there eva", "time to work eva", "hey eva",
             "ok jeva", "are you there", "hey", "help me"]
replay_1 = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir", "nice meeting you again sir!"]

command_2 = [ "bye bye", "bye eva", "go and sleep", "sleep now", "sleep", ]

replay_2 = ["bye sir nice to meet you"," see you again sir","bye sir","bye sir, hope you love my work", "as your wish sir , bye", " it would be great meeting you again sir, bye"]


def Chatterbot(Text):

    for word in Text.split():

        if word in command_1:
            return random.choice(replay_1) + " ,"

        elif word in command_2:
            return random.choice(replay_2) + " ,"

DDD = Chatterbot("bye eva")
print(DDD)