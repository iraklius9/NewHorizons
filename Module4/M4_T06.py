def liters_100km_to_miles_gallon(liters):
    miles = 100 * 1000 / 1609.344
    gallons = liters / 3.785411784
    return miles / gallons


def miles_gallon_to_liters_100km(miles):
    km = miles * 1609.344 / 1000
    liters = 3.785411784
    return 100 / (km / liters)


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
