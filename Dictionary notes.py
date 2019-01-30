states = {
     "CA": "California",
     "FL": "Florida",
     "AK": "Alaska",
     "GA": "Georgia",
}

print(states["CA"])
print(states["AK"])

complex_dictionary = {
     "CA":  {
          "NAME": "California",
          "POPULATION": 39500000,   # 39,500,000
          "CITIES": [
               "Fresno",
               "San Francisco",
               "Los Angeles"
          ]
     },
     "FL": {
          "NAME": "Florida",
          "POPULATION": 21300000,
          "CITIES": [
               "Miami",
               "Orlando",
               "Tampa",
               "Jacksonville"
          ]
     },
     "AK": {
          "NAME": "Alaska",
          "POPULATION": 737000,
          "CITIES": [
               "Atlanta",
               "Savannah",
               "Augusta"
          ]
     }
}

print(complex_dictionary["GA"]["POPULATION"])
print(complex_dictionary["FL"]["NAME"])

georgia = complex_dictionary["GA"]
print(georgia)

print(complex_dictionary["AK"]["CITIES"][0])

print(complex_dictionary.keys())
print(complex_dictionary.items())

for key, value in complex_dictionary.items():
     print(key)
     print(value)
     print("_" * 20)
     # This is what makes it look pretty
print()
for state, info in complex_dictionary.items()



