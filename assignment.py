drinks = ["tea", "coffee", "water"]
chosen_drink = drinks[1]
print(chosen_drink)
print(len(drinks))

# 1. What does each print statement display? Explain why drinks[1] selects that drink.
# Your answer: The first print displays "coffee" because chosen_drink = drinks[1] and Python list indexes start at 0, s drinks[1] is "coffee", not tea becuase tea is 0.
# The second print displays 3 because len(drinks) counts the number of items in the list, and there are three elements: tea, coffee, and water.

# 2. What are the Python types of drinks and chosen_drink?
# Your answer: drinks is a list because it is a collection of values enclosed in square brackets. 
# chosen_drink is a string variable because it stores one text value, "coffee".
