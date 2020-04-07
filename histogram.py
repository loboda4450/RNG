import matplotlib.pyplot as plotter

def main():
    with open("output.txt", "r") as file:
        readed = file.readlines()
        f0 = []
        for line in readed:
            f0.append(int(line.strip()))

    file.close()

    plotter.hist(f0, 15)
    plotter.show()


if __name__ == '__main__':
    main()