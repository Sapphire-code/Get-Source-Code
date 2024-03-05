from bs4 import BeautifulSoup
import requests
import sys
import os
import time
def main():
                websiteUrl = input("Enter website url: ")
                print("Your Websites source code")
                print("==========================================================================")
                getWebsiteUrl = requests.get(websiteUrl)
                soup = BeautifulSoup(getWebsiteUrl.text, 'lxml')
                ask = input("""
		Do you want to print the source code in the console or 
                do you want to save it to an html file?(press y for printing to console
                and press n for saving it to an html file): """)
                if ask == "y":
                    print(soup.prettify())
                else:
                    prettyCode = soup.prettify()
                    f = open('websiteUrl.html', "w")
                    f.write(prettyCode)
                    f.close()


if __name__ == "__main__":
    main()