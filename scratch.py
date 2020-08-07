from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re


def get_url():
    contents = requests.get('https://api.covid19api.com/summary').json()
    # print(contents["Countries"])
    want = contents["Countries"]
    print(want[1]['NewConfirmed'])
    # return url


def main():
    get_url()


if __name__ == '__main__':
    main()
