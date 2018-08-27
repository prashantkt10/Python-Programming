## 1. Programming And Data Science ##

print(1288)
print(639)
print(1288 + 639)

## 2. Arithmetic Operators ##

print((749+371+828+503+1379)/5)

## 3. Variables ##

albuquerque = 749
anaheim = 371
anchorage = 828
arlington = 503
atlanta = 1379
print(anaheim)

## 4. Data Types ##

atlanta_string = "Atlanta"
atlanta_float = 1379.5

## 5. The Type Function ##

hello = 'Hello'
hello_type = type(hello)
print(hello_type)

## 6. Using A List To Store Multiple Values ##

cities = []
crime_rates = []

cities.append("Albuquerque")
cities.append("Anaheim")
cities.append("Anchorage")
cities.append("Arlington")
cities.append("Atlanta")

crime_rates.append(749)
crime_rates.append(371)
crime_rates.append(828)
crime_rates.append(503)
crime_rates.append(1379)

print(cities)
print(crime_rates)

## 7. Creating Lists With Values ##

crime_rates = [749, 371, 828, 503, 1379]

## 8. Comments ##

crime_rates = [749, 371, 828, 503, 1379]
print(crime_rates) 

## 9. Accessing Elements In A List ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]
anchorage_str = cities[2]
anchorage_cr = crime_rates[2]

## 10. Retrieving The Length Of A List ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]
two_sum = len(cities) + len(crime_rates)

## 11. Slicing Lists ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]

cities_slice = cities[1:len(cities)-1]
cr_slice = crime_rates[3:len(crime_rates)]