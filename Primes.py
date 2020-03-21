class Primes:
    def __init__(self, range_from, range_to):
        self.primes = []
        self.user_from = range_from
        self.user_to = range_to + 3
        try:
            for i in range(self.user_from, self.user_to):
                for x in range(2, i):
                    if (i % x) == 0:
                        break
                else:
                    self.primes.append(i)
        except Exception as e:
            print(e)

    def display(self):
        for i in self.primes:
            print(i)

    def get_higher(self, user_val):
        try:
            i = 0
            lowest = self.primes[i]
            while lowest < user_val:
                i = i + 1
                lowest = self.primes[i]

            return self.primes[i]
        except Exception as e:
            print(e)

    def get_lower(self, user_val):
        try:
            i = 0
            lowest = self.primes[i]
            while lowest < user_val:
                i = i + 1
                lowest = self.primes[i]

            return self.primes[i - 1]
        except Exception as e:
            print(e)
