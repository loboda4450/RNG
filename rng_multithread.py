import multiprocessing
import sys
import os

from PIL import ImageGrab
import time
import Primes
import RNGutils


def get_seed_from_pixel():
    image = ImageGrab.grab()
    w, h = image.size
    w_cord = round(time.time() * 1000) % w
    h_cord = round(time.time() * 1000) % h
    pixel_values = image.load()
    pixel = pixel_values[w_cord, h_cord]
    mean_pixel_value = sum(pixel, 0) / len(pixel)

    return round(mean_pixel_value)


def worker(seed, length, threads, rnd_range):
    primes = Primes.Primes()
    rng = RNGutils.RNGutils()

    with open("output.txt", "a+") as file:
        [file.write(f'{number}\n') for number in rng.sequence(primes=primes, pixel_seed=seed, length=int(length / threads),
                                    rnd_range=rnd_range)]

    file.close()

    return


def main():
    try:
        os.remove('output.txt')
        print('removed output file!')
    except Exception as e:
        print(f'Error: {e}')

    start = time.time()
    processes = []

    for i in range(int(sys.argv[3])):
        p = multiprocessing.Process(target=worker, args=(get_seed_from_pixel(), int(sys.argv[1]), int(sys.argv[3]), int(sys.argv[2])))
        processes.append(p)
        p.start()


    for process in processes:
        process.join()

    end = time.time()

    print(f'{sys.argv[1]} random numbers sequence generated in {end - start}')


if __name__ == '__main__':
    main()
