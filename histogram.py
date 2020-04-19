import matplotlib.pyplot as plotter

def main():
    with open("output.txt") as f:
        plotter.hist([int(line.strip()) for line in f if line], 256)
    plotter.show()

if __name__ == '__main__':
    main()
