from PIL import ImageGrab
import time
from Primes import Primes


def get_seed_from_pixel():
    image = ImageGrab.grab()
    w, h = image.size
    w_cord = round(time.time()) % w
    h_cord = round(time.time()) % h
    pixel_values = image.load()
    pixel = pixel_values[w_cord, h_cord]
    mean_pixel_value = sum(pixel, 0) / 3
    return round(mean_pixel_value)


def main():
    primes = Primes()
    pixel_seed = get_seed_from_pixel()
    first_higher = Primes.getFirstHigher(primes, pixel_seed)
    first_lower = Primes.getFirstLower(primes, pixel_seed)
    return f'pixel_seed = {pixel_seed}\nFirst higher = {first_higher}\nFirst lower = {first_lower}\n'


if __name__ == '__main__':
    with open("output.txt", "w+") as file:
        for i in range(10):
            file.write(main())
            time.sleep(0.5)

    file.close()
    # time.sleep(1)
    # print(main())
