import requests


def finder(value):
    # get contents from api(list of all countries whose data is available)
    countryName = []
    country = []
    contents = requests.get('https://api.covid19api.com/summary').json()
    countries = contents["Countries"]
    for item in countries:
        countryName.append(item['Country'])

    # check = input('Enter Value: ')

    # check if value is among country list
    res = [idx for idx in countryName if idx[0].lower() == value.lower()]
    for item in res:
        country.append([item])
    print(country)
    return country
