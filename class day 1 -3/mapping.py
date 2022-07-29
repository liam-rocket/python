# Create a map from name to index
def name_to_index(list_of_names):
  d = {}
  for index, name in enumerate(list_of_names):
    d[name] = index
  return d

# Create a map from index to name
def index_to_name(list_of_names):
  d = {}
  for index, name in enumerate(list_of_names):
    d[index] = name
  return d

tournament_finishers = ["eng liang", "perry", "sam"]
nti = name_to_index(tournament_finishers)
itn = index_to_name(tournament_finishers)

print(nti) # {'perry': 1, 'sam': 2, 'eng liang': 0}
print(itn) # {0: 'eng liang', 1: 'perry', 2: 'sam'}
 
# given a name, get their place in the tournament
nti["perry"] # 1 ==> perry got 2nd

# given a place, get the name of that person
itn[1] # perry was in 2nd place