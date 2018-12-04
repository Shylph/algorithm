# LRU cache reference : https://www.kunxi.org/blog/2014/05/lru-cache-in-python/
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1


def solution(cacheSize, cities):
    process_time = 0
    if cacheSize != 0:
        cache = LRUCache(cacheSize)
        for city in cities:
            if cache.get(city.lower()) == -1:
                cache.set(city.lower(), city)
                process_time += 5
            else:
                process_time += 1
    else:
        process_time = len(cities) * 5

    return process_time


cacheSize = [3, 3, 2, 5, 2, 0]
cities = [["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
          ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
          ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
          ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
          ["Jeju", "Pangyo", "NewYork", "newyork"],
          ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]
out = [50, 21, 60, 52, 16, 25]

for i in range(len(cities)):
    if out[i] == solution(cacheSize[i], cities[i]):
        print(i, "true")
    else:
        print(i, "false : expect :", out[i], " : but :",  solution(cacheSize[i], cities[i]))
