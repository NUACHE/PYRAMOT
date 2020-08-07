# from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from requests import get


# import re


def get_url():
    contents = requests.get('https://api.covid19api.com/summary').json()
    # print(contents["Countries"])

    

    globalContent = contents["Global"]
    want = contents["Countries"]
    print(want[1]['NewConfirmed'])
    choice = input("Enter what you want")
    if choice == 'globalContent':
        print(globalContent['NewConfirmed'])

    # return url


def main():
    get_url()


if __name__ == '__main__':
    main()
