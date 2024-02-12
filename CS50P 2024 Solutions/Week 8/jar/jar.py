class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return self.cookies * "🍪"

    def deposit(self, n):
        if n + self.cookies > self._capacity or n < 0:
            raise ValueError("Too many cookies")
        self.cookies += n

    def withdraw(self, n):
        if n > self.cookies or n < 0:
            raise ValueError("You don't have enough cookies")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
