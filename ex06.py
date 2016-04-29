# operacje na listach
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', checked')

# prawy przedział w range jest otwarty, lewy domknięty [1, 6)
for value in range(1, 6):
    print(value)

numbers = list(range(1, 101))
print(numbers)

# range ze skokiem co 2
even = list(range(2, 101, 2))
print(even)

odd = list(range(1, 101, 2))
print(odd)

squares = []
# możemy iterować od razu po range, bez generowania listy
# range to typ (klasa), sekwencja liczb (immutable)
for value in list(range(1, 101)):
    squares.append(value ** 2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

# list comprehension
comprehension = [value ** 2 for value in range(1, 101)]
print(comprehension)

# slices
# lewy domknięty, prawy otwarty [0, 10)
print(squares[0:10])
# zaczynamy od początku listy
print(squares[:20])
# do ostatniego elementu listy
print(squares[90:])
# jedziemy od końca
print(squares[-10:])

for number in squares[:10]:
    print(number)

# klon listy
squares_copy = squares[:]
print(squares_copy)

# referencja do listy
magicians_ref = magicians
magicians_ref.append('gulci')
print(magicians)

print('list comprehension ze skokiem co 10')
print(comprehension[9::10])
print('długość listy: ' + str(len(comprehension)))
