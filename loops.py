# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Will', 'Janet', 'Karen']

# Simple for loop
# for person in people:
#   print('Current person: ', person)

# Break out
# for person in people:
#   if person == 'Janet':
#     break
#   print('Current person: ', person)

# Continue
# for person in people:
#   if person == 'Janet':
#     continue
#   print('Current person: ', person)

# Range
# for i in range(len(people)):
#   print('Current Person: ', people[i])

count = []
for i in range(0, 11):
  count.append(i)
  print('Number ', i)
  
print(len(count))

# While loops execute a set of statements as long as a condition is true.
# count = 0
# while count <= 10:
#   print('Count: ', count)
#   count += 1