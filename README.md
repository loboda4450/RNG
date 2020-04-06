# Nested Random Number Generator 
Implementation of DOI: 10.23956/ijarcsse/SV7I5/0327 article in Python 3.8, uses PIL and time libs.

Implementation could be better (just use Sieve of Eratosthenes to generate primes, not this shit I wrote) - still tho it's quite fast (generates 100k random numbers in less than a second, 100 milion in about 230secs). It's not the perfect one, but good tradeoff in terms of time complexity and results (You should not use this one to protect your data, cuz it takes a screenshot after executing XD)

Histogram for 100k 8bit numbers (10 bins):
![Histogram](https://raw.githubusercontent.com/loboda4450/RNG/master/hist.png)

