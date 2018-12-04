data = [{"id": 1, "name": "강", "money": 10000},
        {"id": 2, "name": "상", "money": 20000},
        {"id": 3, "name": "훈", "money": 15000}]


import operator

print(data)
print(sorted(data, key=operator.itemgetter("money")))

dict = {"abcde": 7, "fzowe": 5, "fko": 5}
print([item[0] for item in dict.items()])
print(sorted(dict.items()))
print(sorted(dict.items(), key=operator.itemgetter(1)))
print(sorted(dict.items(), key=operator.itemgetter(1, 0)))
print(sorted(dict.items(), key=operator.itemgetter(1, 0), reverse=True))

