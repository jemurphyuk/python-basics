# define a dictionary with the following keys

# beginning
# middle
# end
# hero

# populate the values of keys, with a story broken into beginning middle and end and hero
# print the story using by by calling your dictionary keys individually
# interpolate
marvel_hero = input('Who is your favourtie marvel character to replace Captain America?    ')
hero_gender = input('Are they male, female or prefer not to say?    ')
hero_age = input('How old is your hero?    ')
hero_dictionary = {'beginning': 'The First Avenger',
                   'middle': 'Winter Soldier',
                   'end': 'Civil War',
                   'hero':
                       {'name': marvel_hero,
                        'age': hero_age,
                        'gender': hero_gender,
                    }
                   }

print(hero_dictionary['hero']['name'], hero_dictionary['beginning'])
print(hero_dictionary['hero']['age'], hero_dictionary['middle'])
print(hero_dictionary['hero']['gender'], hero_dictionary['end'])