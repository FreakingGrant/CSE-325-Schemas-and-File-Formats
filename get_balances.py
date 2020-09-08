# Write a function, named "get_balances", that takes a single argument, a string that is in the CSV format.
# The first line of this multiline string argument is the header row and has the names of 4 columns:
#
#       User: The name of a user of the bank
#       Amount: The (integer) amount of money involved in a transaction
#       Transaction: Whether the transaction is a "Deposit" or a "Withdraw"
#       Notes: Any additional information regarding the transaction.
#
# The function should return a dictionary that maps each user's name to their final balance
# (assume all balances start at 0).
# Note, the columns can be in any order

import csv


def get_balances(csv_string):
    user_balances = {}

    # Takes the input csv_string and returns it as an array of dictionaries, with the keys for the entries
    # as the first line from the csv_string
    input_as_dictionary = csv.DictReader(csv_string.splitlines())

    # iterate through the array of dictionaries and make the appropriate calculations
    for row in input_as_dictionary:
        change = 1
        if row["Transaction"] == "Withdraw":
            change = -1

        if row["User"] not in user_balances:
            user_balances[row["User"]] = int(row["Amount"]) * change
        else:
            user_balances[row["User"]] += int(row["Amount"]) * change

    return user_balances
