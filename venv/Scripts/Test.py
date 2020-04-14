import csv

male_age = []
female_age = []
total_age = []
male_pop = []
female_pop = []
total_pop = []

census = open('C:\\Users\\J.Fulford85\\PycharmProjects\InfinityCharacterGenerator\\venv\\nc-est2014-agesex-res.csv')
readingthis = census.readline()

for line in census:
    linesplit = line.split(',')
    sex = (int(linesplit [0]))
    ages = (int(linesplit [1]))
    population = (int(linesplit[2]))
    if(sex == 0):
        total_age.append(ages)
        total_pop.append(population)
    if(sex == 1):
        male_age.append(ages)
        male_pop.append(population)
    if(sex==2):
        female_age.append(ages)
        female_pop.append(population)

census.close()

mage1 = []
mage2 = []
mage3 = []
mage4 = []
mage5 = []
mage6 = []
mage7 = []
mage8 = []
mage9 = []
mage10 = []

for i in male_age:
    if 0.0 <= i <= 9.0:
        mage1.append(male_pop[i])
    if 10.0 <= i <= 19.0:
        mage2.append(male_pop[i])
    if 20.0 <= i <= 29:
        mage3.append(male_pop[i])
    if 30 <= i <= 39:
        mage4.append(male_pop[i])
    if 40 <= i <= 49:
        mage5.append(male_pop[i])
    if 50 <= i <= 59:
        mage6.append(male_pop[i])
    if 60 <= i <= 69:
        mage7.append(male_pop[i])
    if 60 <= i <= 69:
        mage7.append(male_pop[i])