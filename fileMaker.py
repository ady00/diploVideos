import os

countries = ["Austria", "Germany", "England", "Russia", "Turkey", "Italy", "France"]
suffixes = ["Two", "Three", "Finale"]

for suffix in suffixes:
    for country in countries:
        filename = f"{country}{suffix}.txt"
        with open(filename, 'w') as f:
            pass  #  should be empty methinks
