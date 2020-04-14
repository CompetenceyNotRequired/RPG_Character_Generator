import random
min = 1
max = 20
factionTable = []
homeworldTable = 0
socialStatusTable = 0
rand = random.randrange(1, 20, 1)
sixrand = random.randrange(1, 6, 1)

if 11 <= rand <= 16:
    factionTable.append(rand)
    factionTable.append(random.randrange(1, 20, 1))
elif rand == 20:
    factionTable.append(random.randrange(1, 20, 1))
    factiontable.extend(random.randrange(1, 20, 1))
else:
    factionTable.append(rand)

print (factionTable)

