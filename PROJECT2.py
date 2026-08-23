# Project name : LFU Cache
class LFUCache():
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.order = []

    def get(self,key):
        if key in self.cache:
            self.freq[key] += 1
            return self.cache[key]
        else:
            return -1

    def put(self,key,value):
        if key in self.cache:
            self.cache[key] = value
            self.freq[key] += 1
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
                self.freq[key] = 1
                self.order.append(key)
            else:
                min_usage = 999999
                target = None
                for i in self.cache:
                    kamtarin = self.freq[i]
                    if kamtarin < min_usage:
                        min_usage = kamtarin
                        target = i
                    if kamtarin == min_usage:
                        if self.order.index(i) > self.order.index(target):
                            target = i
                self.order.remove(target)
                self.cache.pop(target)
                self.freq.pop(target)

                self.cache[key] = value
                self.freq[key] = 1
                self.order.append(key)

#Test
my_cache = LFUCache(3)

my_cache.put("data1", 500)
my_cache.put("data2", 700)
my_cache.put("data3", 900)

print(my_cache.get("data1"))

my_cache.put("D", 1200)

print(my_cache.get("B"))

print(my_cache.get("D"))   