def main():
    report = open("./input.txt", "r")
    lines = report.readlines()

    for i, line1 in enumerate(lines, start=0):
        n1 = int(line1)
        for y, line2 in enumerate(lines, start=0):
            if i <= y:
                continue

            n2 = int(line2)
            for z, line3 in enumerate(lines, start=0):
                if y <= z:
                    continue

                n3 = int(line3)

                if n1 + n2 + n3 == 2020:
                    print(n1 * n2 * n3)

if __name__ == '__main__':
    main()