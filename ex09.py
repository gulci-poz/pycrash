# słowniki
alien_o = {'color': 'green', 'points': 5}

# przy konkatenacji ze stringiem rzutujemy słownik na string
print('aline_o: ' + str(alien_o))
print(alien_o['color'])
print(alien_o['points'])

alien_o['x_position'] = 0
alien_o['y_position'] = 25
alien_o['speed'] = 'slow'
print(alien_o)

npc_main = {}
print('user: ' + str(npc_main))

npc_main['color'] = 'red'
npc_main['points'] = 100
print('npc_main: ' + str(npc_main))

alien_o['speed'] = 'medium'
alien_o['meta'] = 'none'

if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_o['x_position'] += x_increment
print('alien_o, new position: ' + str(alien_o))

del alien_o['meta']
print(alien_o)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, lang in favorite_languages.items():
    print('name(key): ' + name + '\tlanguage(value): ' + lang)

# domyślny loop w słowniku, wystarczyło by napisać
# for name in favorite_languages:
for name in sorted(favorite_languages.keys()):
    print(name.title() + '\t' + favorite_languages[name])

if 'c++' not in favorite_languages.values():
    print('messy language c++')

# metody keys i values zwracają listy kluczy/wartości
# możemy utworzyć zbiór unikalnych wartości podając listę do set
languages = set(favorite_languages.values())
print(languages)

# można robić loop od razu po set
for lang in set(favorite_languages.values()):
    print(lang)

# lista jako wartość elementu słownika
rivers = {
    'Odra': ['Polska', 'Czechy'],
    'Warta': ['Polska'],
    }

print(rivers.values())

# lista słowników
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# słownik jako wartość elementu słownika
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie-sklodowska',
        'location': 'paris',
        },
    }

# title zmieni też na wielką literę w słowie po myślniku
for username, user_info in users.items():
    print(username)
    print(user_info['first'].title() + ' ' + user_info['last'].title())

for username in sorted(users.keys()):
    print(username)
    # podwójny indeks przy bezpośrednim odwołaniu do słownika wewnątrz
    print(users[username]['first'].title() +
          ' ' +
          users[username]['last'].title())
