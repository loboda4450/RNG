import sys
from PIL import ImageGrab
import time
import Primes
import RNGutils
import matplotlib.pyplot as plotter


def check_sysargs(sysargs):
    if sysargs[1] == '--single':
        args = 3
        if len(sysargs) != args:
            print(f'You provided {len(sysargs) - 1} out of {args} required arguments')
            sys.exit()
        else:
            print(f'mode: {sysargs[1]},\nrandom number range: {sysargs[2]}')
            pass
    elif sysargs[1] == '--sequence':
        args = 4
        if len(sysargs) != args:
            print(f'You provided {len(sysargs) - 1} out of {args} required arguments')
            sys.exit()
        else:
            print(f'mode: {sysargs[1]},\nsize of sequence: {sysargs[2]},\nrandom number range: {sysargs[3]}')
            pass
    else:
        print(f'Wrong mode "{sysargs[1]}" \nAvailable --single [range], --sequention [sequence size] [range]')


def get_seed_from_pixel():
    image = ImageGrab.grab()
    w, h = image.size
    w_cord = round(time.time() * 1000) % w
    h_cord = round(time.time() * 1000) % h
    pixel_values = image.load()
    pixel = pixel_values[w_cord, h_cord]
    mean_pixel_value = sum(pixel, 0) / len(pixel)

    return round(mean_pixel_value)


def main():
    check_sysargs(sys.argv)  # check if user defined all required parameters

    primes = Primes.Primes()
    rng = RNGutils.RNGutils()
    seed = get_seed_from_pixel()
    random_array = []

    if sys.argv[1] == "--sequence":
        start = time.time()
        with open("output.txt", "w+") as file:
            [(file.write(f'{number}\n'), random_array.append(number)) for number in rng.sequence(primes=primes, pixel_seed=seed, length=sys.argv[2], rnd_range=int(sys.argv[3]))]

        file.close()
        end = time.time()

        plotter.hist(random_array, int(sys.argv[3]))
        plotter.show()

        print(f'{sys.argv[2]} random numbers sequence generated in {end - start}\nentropy: {rng.entropy}')

    elif sys.argv[1] == "--single":
        print("Single mode\n")
        with open("output.txt", "w+") as file:
            string = f'{rng.single(primes=primes, pixel_seed=seed, rnd_range=int(sys.argv[2]))}\n'
            if "-" not in string:
                file.write(string)
                print(string)

        file.close()


if __name__ == '__main__':
    main()
