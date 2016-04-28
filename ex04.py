# listy
# listy - tablice w py
# możemy przechowywać elementy różnego typu
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 8]
print(bicycles)
print(bicycles[3])
# ostatni element listy
print(bicycles[-1])
# pierwszy element listy
# odczytywanie listy od końca - indeksujemy ujemnie od 1
print(bicycles[-len(bicycles)])
bicycles[0] = 'racing'
print(bicycles)
bicycles.append('trek')
print(bicycles)

# pycharm będzie sugerował użycie literału listy, jeśli będziemy używali append
# zaraz po deklaracji pustej listy
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# indeks nowego elementu
motorcycles.insert(1, 'ducati')
print(motorcycles)

# usuwanie za pomocą del i indeksu
del motorcycles[2]
print(motorcycles)
# pop zwraca usunięty z listy element
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)
# usuwanie za pomocą pop i indeksu
print(motorcycles.pop(0))
print(motorcycles)
# usuwanie za pomocą remove, usuwa tylko pierwsze wystąpienie elementu
motorcycles.remove('ducati')
print(motorcycles)
