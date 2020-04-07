# Nested Random Number Generator 
Implementation of DOI: 10.23956/ijarcsse/SV7I5/0327 article in Python 3.8, uses PIL and time libs.

## Singlethread
Implementation could be better (just use Sieve of Eratosthenes to generate primes, not this shit I wrote) - still tho it's quite fast (generates 100k 8bit random numbers in less than a second, 100 milion 8bit in about 230secs). It's not the perfect one, but good tradeoff in terms of time complexity and results (You should not use this one to protect your data, cuz it takes a screenshot after executing XD)

### Executing:

```rng.py --single [range of random numbers]```
```rng.py --sequence [size of sequence] [range of random numbers]```

## Multithread
Implementation is same as singlethread, but I've added workers, that distribute the same amount of work for each one. What's more, checking for sys.argv is removed, same as --single mode, cuz multithread version is faster only when we generate over 1 milion numbers ( 100 milion 8bit takes ~25secs on stock Ryzen 7 2700 using all 16 threads instead of 230secs).

### Executing:
```rng_multithread.py [size of sequence] [range of random numbers] [threads amount you want to use]```

Histogram for 100k 8bit numbers (10 bins, singlethread):
![Histogram](https://raw.githubusercontent.com/loboda4450/RNG/master/hist.png)

