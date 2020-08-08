import requests
import data


def main():
    # get contents from api
    contents = requests.get('https://api.covid19api.com/summary').json()
    countries = contents["Countries"]

    # get user's country code by using public ip
    countryCode = data.user_data()

    # find the name of the country with that country code
    country = data.find(countries, countryCode)
    print(country)

    # enter the covid info you want to know
    choice = input("Enter what you want")
    data.choice_to_number(choice, countries, countryCode)


if __name__ == '__main__':
    main()
