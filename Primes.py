def isPrime(value):
    if value > 1:  # every prime value is bigger than 1
        for divisor in range(2, value):  # every prime value is dividable by 1
            if value % divisor == 0:
                return True

        return False


class Primes:
    def __init__(self):
        self.higher_prime = None
        self.lower_prime = None
        self.prime = None

    def getPrimeValue(self):
        if self.prime is not None:
            return self.prime
        else:
            return None

    def getFirstHigher(self, value):
        local_var = value
        while isPrime(local_var):
            local_var = local_var + 1

        self.higher_prime = local_var
        return self.higher_prime

    def getFirstLower(self, value):
        local_var = value
        while isPrime(local_var):
            local_var = local_var - 1

        self.lower_prime = local_var
        return self.lower_prime
        pass
