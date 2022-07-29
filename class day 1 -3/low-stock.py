from random import choice

"""Example 2: Determine low-stock items"""

# Generate fruits in a supermarket
fruit_types = ["apple","pear","banana"]
fruits = [choice(fruit_types) for _ in range(1000)]

# Compile a tally of how many times an element appears in an array
def get_low_stock(ls_of_fruits, threshold):
  ''' Return names of stock that are low (below threshold, an int) '''
  # Compile tally
  tally = {}
  for fruit in fruits:
    if fruit not in tally:
      tally[fruit] = 1
    else:
      tally[fruit] += 1

  # Compile elements in tally that have a count below a threshold
  result = []
  for fruit, count in tally.items():
    if count < threshold:
      result.append(fruit)
  return result

# Output low-stock items
print(get_low_stock(fruits, 330))
