# Write a function, named "sum_all_JSON_numbers" that takes a string with a JSON object as its contents.
# The function should return the sum of every JSON number in the string

import json


def parse_dictionary(dictionary):
    total = 0

    for key in dictionary:
        value = dictionary[key]

        if isinstance(value, bool):
            pass
        elif isinstance(value, (int, float)):
            total += value
        elif isinstance(value, list):
            total += sum_array(value)
        elif isinstance(value, dict):
            total += parse_dictionary(value)

    return total


def sum_array(arr):
    total = 0
    for num in arr:
        if isinstance(num, (int, float)):
            total += num

    return total


def sum_all_JSON_numbers(input_string):
    total = 0

    # Takes the input JSON string and returns it back as a Python Dictonary
    dictionary = json.loads(input_string)

    # Go through the dictionary and extract the sum of all numbers
    total += parse_dictionary(dictionary)

    return total


test_string = '{"name":"josh", "age":31, "instructor":true, "degree dates": [2005, 2006, 2013], "pets":["CrashDown", "Ghost", "RaceTrack", "Dany"]}'
input_string = '{"name":"josh", "age":"31", "instructor":true, "courses": [232, 480, 431, 220, 491, 830, 450], "degree dates": {"hs": 2005.6, "bs":2006, "phd":2013}, "pets":["CrashDown", "Ghost", "RaceTrack", "Dany"]}'

print(sum_all_JSON_numbers(test_string))
print(sum_all_JSON_numbers(input_string))
