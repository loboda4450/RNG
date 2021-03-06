# Nested Random Number Generator 
Implementation of DOI: [10.23956/ijarcsse/SV7I5/0327](http://ijarcsse.com/Before_August_2017/docs/papers/Volume_7/5_May2017/SV7I5-0327.pdf) article in Python 3.8, uses PIL, time, numpy and math libs.

### It's not the best RNG algorithm, you'd better not to use it, there is "fixed" version in my repos ([RNGvideo](https://github.com/loboda4450/RNGvideo)). It's still not perfect in terms of optimization, but will work on it soon.

### Singlethread
Implementation could be better (just use Sieve of Eratosthenes to generate primes, not this shit I wrote) - still tho it's quite fast (generates 100k 8bit random numbers in less than a second, 100 milion 8bit in about 230secs). It's not the perfect one, but good tradeoff in terms of time complexity and results (You should not use this one to protect your data, cuz it takes a screenshot after executing XD)

##### Executing:

```python rng.py --single [range of random numbers]```

```python rng.py --sequence [size of sequence] [range of random numbers]```

### Multithread
Implementation is same as singlethread, but I've added workers, that distribute the same amount of work for each one (with new seed value). What's more, checking for sys.argv is removed, same as ```--single``` mode, cuz multithread version is faster only when we generate over 1 milion numbers (100 milion 8bit takes ~25secs on stock Ryzen 7 2700 using all 16 threads instead of 230secs). It's still not a optimal solution, cuz it consumes huge amount of RAM. __Remember to clean the output.txt before every trigger, cuz in multithread version each worker append his part to output.txt file__ (u won't end up with over 5GB .txt file, same as me XD...)

##### Executing:
```python rng_multithread.py [size of sequence] [range of random numbers] [threads amount you want to use]```

### Histogram for 100k 8bit numbers (10 bins, singlethread):
![Histogram](https://raw.githubusercontent.com/loboda4450/RNG/master/hist.png)

