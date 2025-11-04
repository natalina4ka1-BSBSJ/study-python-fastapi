base_list = [1, 2, 3]
print(len(base_list))

base_list.append(4)
print(base_list)

base_list.extend([5, 6, 7])
print(base_list)

print(base_list.index(4))

base_dict = {"name": "Tom", "age": 40, "hiht": 180}
print(base_dict.keys())
print(base_dict.values())
print(base_dict.items())
print(base_dict["name"], base_dict.get("name"))

base_dict = {"name": "Tom", "age": 40, "hiht": 180}
print(base_dict.keys())
print(base_dict.values())
print(base_dict.items())
print(base_dict["name"], base_dict.get("is animal", "no"))