def city_country(city, country):
    print(city + "," + country)


while True:
    cityName = input("city name is : ")
    if cityName == 'q':
        break
    countryName = input("country name is : ")
    if countryName == 'q':
        break
    city_country(cityName, countryName)
