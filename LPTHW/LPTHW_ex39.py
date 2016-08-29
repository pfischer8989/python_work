__author__ = 'pfischer'

# Create map of provinces

provinces = {'British Columbia': 'BC',
             'Alberta': 'AB',
             'Ontario': 'ON',
             'Quebec': 'QB',
             'Newfoundland': 'NB'
}

cities = {
            'AB': 'Calgary',
            'ON': 'Toronto',
            'QB': 'Montreal'

}

# add more cities
cities['BC'] = 'Vancouver'
cities['NB'] = 'Halifax'

# print out some cities
print ('-' * 10)
print ("BC has: ", cities['BC'])
print ("NB has: ", cities['NB'])

# print some provinces
print ('-' * 10)
print("Ontario's abbreviation is: ", cities[provinces['Ontario']])
print("Quebec's abbreviation is: ", cities[provinces['Quebec']])

# do it by using the prov then the cities dict
print('-' * 10)
print("Alberta has: ", cities[provinces['Alberta']])
print("British Columbia has: ", cities[provinces['British Columbia']])

# print all prov abbrev
print('-' * 10)
for provinces, abbrev in provinces.items():
    print("%s is abbreviated %s" % (provinces, abbrev))

# print all cites
print('-' * 10)
for abbrev, city in cities.items():
    print ("%s has the city %s" % (abbrev, city))

# now at the same time
print('-' * 10)
for provinces, abbrev in provinces.items():
    print("%s state is abbreviated %s and has city %s" % (provinces, abbrev, cities[abbrev]))


print('-' * 10)
prov = provinces.get('Texas')

if not prov:
    print ("Sorry no TExas")

city = cities.get('TX', 'Does not exist')
print("The city for the prov 'TX' is: %s" % city)





