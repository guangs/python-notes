# https://www.workat.tech/problem-solving/practice/lru-cache

# ./resources/011-lru-cache.png
# https://www.youtube.com/watch?v=9sUusiJSYRc


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.least_used = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.least_used.remove(key)
            self.least_used.append(key)
            return self.cache[key]
        else:
            return -1

    def add(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.least_used.remove(key)
            self.least_used.append(key)
        else:
            if len(self.cache) >= self.capacity:
                least_used_key = self.least_used.pop(0)
                del self.cache[least_used_key]
            self.cache[key] = value
            self.least_used.append(key)
