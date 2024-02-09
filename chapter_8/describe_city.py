def describe_city(city_name, country_name='the USA'):
    message = f"{city_name.title()} is in {country_name.title()}."
    print(message)

describe_city('scranton')
describe_city('portland')
describe_city('oslo', 'norway')