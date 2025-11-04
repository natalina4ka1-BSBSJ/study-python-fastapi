lst = [1, 2, 3, 4, 5]
dtc = {"name" : "Tom", "age": 5}
name = "Tome"
tpl = ("n", "a", "g")

result = dtc["age"] in lst 
print(result)

lst = [1, 2, 3, 4, 5]
dct = {"name" : "Tom", "age": 5}
name = "Tome"
tpl = ("n", "a", "g")

result = dct["age"] in lst and dct["name"] in tpl
print(result)

lst = [1, 2, 3, 4, 5]
dct = {"name" : "Tom", "age": 5}
name = "Tome"
tpl = ("n", "a", "g")

result = dct["age"] in lst or dct["name"] in tpl
print(result)

lst = [1, 2, 3, 4, 5]
dct = {"name": "Tom", "age": 5}
name = "Tom"
tpl = ("n", "a", "g")

print(dct["name"] == name)

lst = [1, 2, 3, 4, 5]
dct = {"name": "Tom", "age": 5}
name = "Tom"
tpl = ("n", "a", "g")

print(dct["name"] == name and dct ["age"] in lst)