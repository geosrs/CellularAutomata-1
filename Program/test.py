def display():
    recd = open("record.txt")
    grid = []
    rows = int(recd.readline())
    for line in recd:
        grid = makeGrid(decode(line), rows)

    return grid

def decode(line):
    dcd = ""

    for a in line:
        if a.isdigit():
            space = " "*int(a)
            dcd+=space
        else:
            dcd+=a

    return dcd

def makeGrid(gridln, rows):
    grid = []
    rw = []
    for a in gridln:
        for i in range(rows):
            rw.append(a)
        grid.append(rw)
        rw = []

    return grid


if __name__ == "__main__":
    temp = display()

    print temp
