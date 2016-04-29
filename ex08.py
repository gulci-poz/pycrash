# if

cars = ['audi', 'bmw', 'subaru', 'toyota']

# == jest case sensitive; !=; < > <= >=
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age_1 = 17
age_2 = 27

if age_1 >= 18 and age_2 >= 18:
    print('dwoje pełnoletnich pijaków')
else:
    print('przynajmniej jeden nieletni pijak')

if age_1 >= 18 or age_2 >= 18:
    print('przynajmniej jeden pełnoletni pijak')
else:
    print('dwoje nieletnich pijaków')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('Mushrooms: ' + str('mushrooms' in requested_toppings))
print('Pepperoni: ' + str('pepperoni' in requested_toppings))

banned_user = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_user:
    print(user.title() + ', you can post a response if you wish.')

age_list = [4, 35, 5, 10, 78, 64, 32, 18]
price_list = []

for age in age_list:
    if age < 4:
        price_list.append(0)
    elif age < 18:
        price_list.append(5)
    elif age < 65:
        price_list.append(10)
    elif age >= 65:
        price_list.append(5)
    # elif i dokładny warunek zamiast else
    # odrzucamy nieprawidłowe wartości, które przeszły przez if

    print('Wiek: ' + str(age) + ', bilet: ' +
          str(price_list[len(price_list) - 1]))

# przy konkatenacji stringa i listy w print używamy str dla listy
print('Wiek: ' + str(age_list))
print('Bilety: ' + str(price_list))

# sprawdzanie, czy lista nie jest pusta
example_list = []
if example_list:
    print(example_list)
else:
    print('pusta lista')

toppings_menu = ['pieczarki', 'oliwki', 'papryczki', 'salami', 'tuńczyk']
toppings_req = ['papryczki', 'salami', 'tuńczyk', 'frytki']
toppings_ok = []
toppings_out = []
toppings_ok_str = ''
toppings_out_str = ''

for req in toppings_req:
    if req in toppings_menu:
        toppings_ok.append(req)
        toppings_ok_str += req + ', '
    else:
        toppings_out.append(req)
        toppings_out_str += req + ', '

toppings_ok_str = toppings_ok_str.strip()
toppings_ok_str = toppings_ok_str[:len(toppings_ok_str) - 1]
toppings_out_str = toppings_out_str.strip()
toppings_out_str = toppings_out_str[:len(toppings_out_str) - 1]

print('Osiągalne przystawki: ' + toppings_ok_str + '.')
print('Brak przystawek: ' + toppings_out_str + '.')
