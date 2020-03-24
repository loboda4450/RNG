import matplotlib.pyplot as plotter


def main():
    with open("output.txt", "r") as file:
        readed = file.readlines()
        numline = 0
        # b0 = []
        # d0 = []
        f0 = []
        for line in readed:
            numline = numline + 1
            # if numline % 3 == 2:
            #     b0.append(int(line)%10000000000000000000)
            # elif numline % 3 == 1:
            #     d0.append(int(line)%10000000000000000000)
            # if numline % 3 == 0:
            #     if not line.find("-"):
            f0.append(int(line) % 10000000)

    file.close()

    # for i in b0:
    #     print(i)
    #
    # for i in d0:
    #     print(i)
    #
    # for i in f0:
    #     print(i)

    plotter.hist(f0, 25)
    plotter.show()


if __name__ == '__main__':
    main()
