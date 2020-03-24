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
    mean_pixel_value = sum(pixel, 0) / 3
    return round(mean_pixel_value)


def main():
    primes = Primes.Primes()
    rng = RNGutils.RNGutils()
    seed = get_seed_from_pixel()
    if sys.argv[1] == "--sequention":
        with open("output.txt", "a+") as file:
            random_array = rng.sequention(primes, seed, sys.argv[2])
            for number in random_array:
                file.write(f'{number}\n')
                print(number)

        file.close()

    elif sys.argv[1] == "--single":
        print("Chosen single\n")
        with open("output.txt", "a+") as file:
            string = f'{rng.single(primes=primes, pixel_seed=seed)}\n'
            if "-" not in string:
                file.write(string)
                print(string)

        file.close()


if __name__ == '__main__':
    main()
