import sys

from PIL import ImageGrab
import time
import Primes
import RNGutils


def check_sysargs(sysargs):
    if sysargs[1] == '--single':
        args = 3
        if len(sysargs) != args:
            print(f'You provided {len(sysargs) - 1} out of {args} required arguments')
            sys.exit()
        else:
            print(f'mode: {sysargs[1]},\nsize of sequence: {sysargs[2]},\nrandom number range: {sysargs[3]}')
            pass
    elif sysargs[1] == '--sequention':
        args = 4
        if len(sysargs) != args:
            print(f'You provided {len(sysargs) - 1} out of {args} required arguments')
            sys.exit()
        else:
            print(f'mode: {sysargs[1]},\nrandom number range: {sysargs[2]}')
            pass
    else:
        print(f'Wrong mode "{sysargs[1]}" (available --single, --sequention)')


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
    check_sysargs(sys.argv)  # check if user defined all required parameters

    primes = Primes.Primes()
    rng = RNGutils.RNGutils()
    seed = get_seed_from_pixel()
    if sys.argv[1] == "--sequention":
        print("Sequention mode\n")
        with open("output.txt", "a+") as file:
            random_array = rng.sequention(primes=primes, pixel_seed=seed, length=sys.argv[2], rnd_range=int(sys.argv[3]))
            for number in random_array:
                file.write(f'{number}\n')
                print(number)

        file.close()

    elif sys.argv[1] == "--single":
        print("Single mode\n")
        with open("output.txt", "a+") as file:
            string = f'{rng.single(primes=primes, pixel_seed=seed, rnd_range=int(sys.argv[2]))}\n'
            if "-" not in string:
                file.write(string)
                print(string)

        file.close()


if __name__ == '__main__':
    main()
