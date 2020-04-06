import time


class RNGutils:
    def __init__(self):
        self.random_array = []
        self.b0 = None
        self.d0 = None
        self.f0 = None
        self.l0 = None
        self.m = None

    def single_handler(self, lower_prime, higher_prime, rnd_range):
        try:
            self.m = lower_prime * higher_prime
            self.b0 = (lower_prime ** 2) % self.m
            self.d0 = (higher_prime ** 2) % self.m
            self.l0 = int(time.time())*1000
            self.f0 = self.b0 * self.d0 * self.l0 % rnd_range
        except Exception as e:
            print(e)

    def sequention_handler(self, primes, sequention_length, rnd_range):
        for i in range(int(sequention_length)):
            try:
                self.m = primes.lower_prime * primes.higher_prime
                self.b0 = (self.b0 ** 2) % self.m
                self.d0 = (self.d0 ** 2) % self.m
                self.l0 = (self.l0*primes.lower_prime + primes.higher_prime) % self.m
                self.f0 = self.b0 * self.d0 * self.l0 % rnd_range
                self.random_array.append(self.f0)
            except Exception as e:
                print(e)
        pass

    def single(self, primes, pixel_seed, rnd_range):
        primes.getFirstHigher(seed=pixel_seed)
        primes.getFirstLower(seed=pixel_seed)
        self.single_handler(lower_prime=primes.lower_prime, higher_prime=primes.higher_prime, rnd_range=rnd_range)
        return int(self.f0)

    def sequention(self, primes, pixel_seed, length, rnd_range):
        primes.getFirstHigher(seed=pixel_seed)
        primes.getFirstLower(seed=pixel_seed)
        self.single_handler(lower_prime=primes.lower_prime, higher_prime=primes.higher_prime, rnd_range=rnd_range)
        self.sequention_handler(primes=primes, sequention_length=length, rnd_range=rnd_range)
        return self.random_array
