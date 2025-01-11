# names =  ['john', 'peter', 'pan', 'george']
# print(dir(names))
# names.append("mary")
# names.append(True)
# print(names)
# newNames = ['kate', 'fatimah', 'gabe']
# names.extend(newNames)
# print(names)
# we cant really extend just a single data, because assuming use the name segun, it'd 
# return as each character individually added
# names.extend("segun")
# print(names)
# names.insert(2, "segun")
# names.clear() #clear could be used to like reset, 
# del(names) #once dleted u'd see that it shows error after using the print function, it shows error 
# bcause it will not be found
# anotherNames = names.copy()
# names =  ['john', 'john', 'peter', 'pan', 'george']
# name = "john"
# countResult = names.count("john")
# poped = names.pop(1)
# print(poped)
# names.remove("john")
# print(names)

# NESTING
# cars =  ['bmw', 'audi', 'toyota', 'benx']
# cars = [['m5', 'm6'], 'audi', 'toyota', ['AMG', 'GLE']]
# cars[0][1] = "m1"
# print(F'I AM DRIVING A {E}')
# print(cars)

# DICTIONARY; DENOTED BY CURLY BRACES. DIC IS A COLLECTION TYPE THAT STORES VALUE IN A KEY:VALUE TERMS
cars = {
    "bmw" : "m5",
    "audi" : "audi",
    "number" : 4,
    "status": True
    }

cars["status"] = False
ourKeys = list(cars)
print(ourKeys)
