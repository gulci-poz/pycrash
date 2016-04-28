# sortowanie
# sort sortuje listę in place, nieodwracalnie
print('sort')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print('sorted')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

# zmiany zostają zapisane w liście
print('reverse')
cars.reverse()
print(cars)

# dla pustej listy cars[-1] zwróci error
