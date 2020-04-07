import multiprocessing
import sys

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


def worker(seed, length, threads):
    primes = Primes.Primes()
    rng = RNGutils.RNGutils()

    with open("output.txt", "a+") as file:
        random_array = rng.sequence(primes=primes, pixel_seed=seed, length=int(length / threads), rnd_range=int(sys.argv[2]))
        for number in random_array:
            file.write(f'{number}\n')

        file.close()

    return


def main():
    seed = get_seed_from_pixel()

    start = time.time()
    processes = []

    for i in range(int(sys.argv[3])):
        p = multiprocessing.Process(target=worker, args=(seed, int(sys.argv[1]), int(sys.argv[3]),))
        processes.append(p)
        p.start()


    for process in processes:
        process.join()

    end = time.time()

    print(f'{sys.argv[1]} random numbers sequence generated in {end - start}')


if __name__ == '__main__':
    main()
