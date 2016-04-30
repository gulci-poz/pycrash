# stringi
name = "johnny bravo"
print(name.title())
name = "JOHNNY bravo"
print(name.title())
print(name.upper())
print(name.lower())
# title, upper i lower nie modyfikują zmiennej
print(name)

first_name = "johnny"
last_name = "bravo"
name = first_name + " " + last_name
message = "Hello, " + name.title()
print(message)

# jeden tab w środku stringa działa jak spacja, dwa dają spację i tab
# tylko w pyCharm, w konsoli jest ok
print("\ttab\t\ttab")
print("\nnew line")
print("\"quotation")
print('\'apostrophe')

lang = ' python '
print('|' + lang.rstrip() + '|')
print('|' + lang.lstrip() + '|')
# obustronny strip
print('|' + lang.strip() + '|')
# rstrip, lstrip i strip nie modyfikują zmiennej
print('|' + lang + '|')
