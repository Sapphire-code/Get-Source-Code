from bs4 import BeautifulSoup
import requests
import sys
import os
import time
import keyboard
keyboard.press_and_release('f11, shift')
def getsource():
                geta = input("Enter website url: ")
                print("Your Websites source code")
                print("==========================================================================")
                getb = requests.get(geta)
                soup = BeautifulSoup(getb.text, 'lxml')
                ask = input("""
		Do you want to print the source code in the console or 
                do you want to save it to an html file?(press y for printing to console
                and press n for saving it to an html file): """)
                if ask == "y":
                    print(soup.prettify())
                else:
                    vara = soup.prettify()
                    f = open('geta.html', "w")
                    f.write(vara)
                    f.close()


getsource()
