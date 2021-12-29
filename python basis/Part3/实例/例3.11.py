dict1 = {}
print(dict1)
print(type(dict1))
dict2 = {'Jerry': 8, 'Tom': 5, 'Mary': 10}
print(dict2)
dict3 = {'name': 'Tom', 'Age': 22, 'Sex': 'male', 123: 'China USA US'}
print("dict2['Jerry']:", dict2['Jerry'])
dict2['Tom'] = 7
dict2['Mary'] = 12
print(dict2)
del dict3[123]
print(dict3)
dict3.clear()
print(dict3)
