from PIL import ImageGrab
import time
import Primes


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
    pixel_seed = get_seed_from_pixel()
    primes_list = Primes.Primes(range_from=2, range_to=pixel_seed)
    lower = Primes.Primes.get_lower(primes_list, user_val=pixel_seed)
    higher = Primes.Primes.get_higher(primes_list, user_val=pixel_seed)
    return f'pixel_seed = {pixel_seed}\nhigher = {higher},\nlower = {lower}\n'


if __name__ == '__main__':
    with open("output.txt", "w+") as file:
        for i in range(100):
            file.write(main())
            time.sleep(0.5)

    file.close()
    # time.sleep(5)
    # print(main())
