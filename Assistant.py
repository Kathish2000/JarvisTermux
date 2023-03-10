####### MODULE #######
import os
import subprocess
import webbrowser
import random
import datetime
######################
#Greeting 
def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        os.system("termux-tts-speak Good Morning Sir")              
    elif hour >= 12 and hour <18:
        os.system("termux-tts-speak Good AfterNoon sir ")                   
    else:
        os.system("termux-tts-speak Good Evening Sir")
    os.system("termux-tts-speak I am kaira sir please Tell me How may I help You ") 
wishMe()
os.system("clear")

    
while True:
    colour = ["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m"]
    Colour=random.choice(colour)
    print()

    print(Colour," >>>>>[ Say Somthing...! ]<<<<")
    
    print()
    query = subprocess.getoutput("termux-speech-to-text")
    print()
    
    print("\033[41m""\033[32m[>",query, "<]\033[0m")

    
### Start 

    if "hello" in query or "Hi" in query:
        os.system("termux-tts-speak Hello Sir I am kaira")
        print("\033[34m""Hello Sir I am kaira ! \033[0m")

    elif "who are you" in query or "what is your name" in query:
        os.system("termux-tts-speak I am kaira Sir ")
        print("\033[38;5;209m"" I am kaira sir")

    elif "game" in query or "which game" in query:
        os.system("termux-tts-speak You Play terminal hacking")
# Caller         
    elif "call amma" in query or "call my mom" in query:
        os.system("termux-tts-speak I am Calling amma sir ")
        os.system("termux-telephony-call 7708954239")
    elif "call appa" in query or "call my dad" in query:
        os.system("termux-tts-speak I am Calling appa sir ")
        os.system("termux-telephony-call 8300167747")
    elif "call shalini" in query or "call shalni" in query:
        os.system("termux-tts-speak I am Calling Sir ")
        os.system("termux-telephony-call 7448627612")
    elif "battery" in query or "status" in query:
        os.system("termux-tts-speak Here the Current information of your battery")
        os.system("termux-battery-status")
    elif "open Google" in query or "Google" in query:
        os.system("termux-tts-speak Opening google Sir")
        os.system("termux-open-url https://google.com")
    elif "open YouTube" in query or "YouTube" in query :
        os.system("termux-tts-speak Opening youtube Sir")
        os.system("termux-open-url https://YouTube.com")
    elif "what\'s up" in query or "how are you" in query :
        Ms = ['Just doing my Thing ! ', 'I am Fine','Nice', 'I am Nice and Full of energy']
        os.system("termux-tts-speak " + random.choice(Ms))


    elif "play music" in query or "start music" in query or "music" in query : 
        os.system("bash music.sh")
# Termux-api command
    elif "torch on" in query or "light on" in query :
        os.system("termux-torch on")

    elif "torch off" in query or "light off" in query :         os.system("termux-torch off")

    elif "vibrate" in query or "vibrate my device" in query:
        os.system("termux-tts-speak I am Vibrating Your device Sir")
        os.system("termux-vibrate")
    elif "contact list" in query :
        os.system("termux-tts-speak I am Listing your contact List")
        os.system("termux-contact-list")
    elif "brightness" in query :
        os.system("termux-tts-speak What should be the Ratio of brightness ")
        bright = subprocess.getoutput("termux-speech-to-text")
        print(str(bright))
        os.system("termux-brightness " + str(bright))
    elif "exit" in query or "stop" in query or "quit" in query :
        os.system("termux-tts-speak Okay Sir, i'm going bye")
        exit()
    elif "Wi-Fi on" in query:
        os.system("termux-tts-speak I am activating your wifi")
        os.system("termux-wifi-enable true")
    elif "disable Wi-Fi" in query or "Wi-Fi off" in query :
        os.system("termux-tts-speak I am disactivated your wi-fi signal ")
        os.system("termux-wifi-enable true")
    elif "I love you" in query or "love" in query:
        os.system("termux-tts-speak I Love you too Sir")

    elif "search" in query or "find" in query :
        os.system("termux-tts-speak What do you want search For")
        print("\033[32m<<[ \033[33m""What Do You Want \033[31m\033[4mSEARCH \033[33mFor ? \033[32m]>>")
        print()
        command = subprocess.getoutput("termux-speech-to-text")
        print("\033[42m""\033[38;5;209m[>",command, "<]\033[0m")

        os.system("termux-open-url https://www.youtube.com/results?search_query=" + command)
        os.system("termux-tts-speak Here the Search Results About " + command + "From YouTube")
    elif "thanks" in query or "well done" in query:
        os.system("termux-tts-speak No problem Sir Its my pleasure ")

    elif "application" in query or "letter" in query :
        os.system("clear")
        os.system("\033[34m")
        os.system("cat notes_20371010210856.txt")

        



    else :
        os.system("termux-tts-speak Sorry sir ! i did not get that please Speak Again")
        print()
        print("\033[38;5;209m""Sorry sir ! i did not that please Speak Again !\033[0m ")


        

