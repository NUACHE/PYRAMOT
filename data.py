import requests


# find users country from country code
def find(json_object, countryCode):
    return [obj for obj in json_object if obj['CountryCode'] == countryCode][0]['Country']


# find new confirmed cases from country code
def newConfirmed(json_object, countryCode):
    return [obj for obj in json_object if obj['CountryCode'] == countryCode][0]['NewConfirmed']


# find total confirmed cases from country code
def totalConfirmed(json_object, countryCode):
    return [obj for obj in json_object if obj['CountryCode'] == countryCode][0]['TotalConfirmed']


# find new death cases from country code
def newDeaths(json_object, countryCode):
    return [obj for obj in json_object if obj['CountryCode'] == countryCode][0]['NewDeaths']


# find total death cases from country code
def totalDeaths(json_object, countryCode):
    return [obj for obj in json_object if obj['CountryCode'] == countryCode][0]['TotalDeaths']


# find new recovery cases from country code
def newRecovered(json_object, countryCode):
    return [obj for obj in json_object if obj['CountryCode'] == countryCode][0]['NewRecovered']


# find total recovery cases from country code
def totalRecovered(json_object, countryCode):
    return [obj for obj in json_object if obj['CountryCode'] == countryCode][0]['TotalRecovered']


# a switch-like solution to finding cases wanted
def choice_to_number(choice, json_object, countryCode):
    switcher = {
        'totalRecovered': totalRecovered(json_object, countryCode),
        'newRecovered': newRecovered(json_object, countryCode),
        'newDeaths': newDeaths(json_object, countryCode),
        'totalDeaths': totalDeaths(json_object, countryCode),
        'newConfirmed': newConfirmed(json_object, countryCode),
        'totalConfirmed()': totalConfirmed(json_object, countryCode)
    }
    print(switcher.get(choice, "Wrong input"))


# finding user's country code from public ip address
def user_data():
    # even though 'country' is entered, api return country code
    return requests.get('http://ipinfo.io/json').json()['country']
