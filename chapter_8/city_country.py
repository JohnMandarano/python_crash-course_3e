def city_country(city_name, country_name):
    city_and_country = f"{city_name}, {country_name}"
    return city_and_country.title()

print(city_country('scranton', 'pennsylvania'))
print(city_country('amsterdam', 'netherlands'))
print(city_country('mexico city', 'mexico'))