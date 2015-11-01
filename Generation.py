from Animal import lion, antelope
from random import random

def compress(gridstr):
    comprsd = ""
    no = 0
    for a in gridstr:
        if " " == a:
            no+=1
        elif no!=0:
            comprsd+=(str(no)+a)
            no = 0
        else:
            comprsd+=a

    return comprsd

def record(grid):
    line = ""
    for a in range(grid.rows+2):
        for b in range(grid.columns+2):
            # add all the units in one string ("join" doesn't work with objects)
            line+=(str(grid.get(a, b)))

    line = compress(line)
    recfl = open ("record.txt", 'a')
    recfl.write(line+"\n")

    recfl.close()

# a method to run the generations, given by "gen", or until a keyboard interrupt
def run(grid, features, recordgrid):
    """ Run a generation of animals in the grid
    """
    for a in range(grid.rows):
        for b in range(grid.columns):
            cell = grid.get(a+1, b+1)
            # cell is an animal
            if cell != " ":
                # make each animal older
                grid.age(a+1, b+1)

                # old animals die
                if cell.getAge() <0 :
                    grid.set(a+1, b+1, " ")
                # if it is still young and a lion
                elif str(cell).upper() == "L":
                    #random deaths
                    # generate a random no, and if it equals 1 the lion dies
                    if int(random()*32) == 1:
                        grid.set(a+1, b+1, " ")
                    else:
                        area = (grid.area(a, b)).upper()
                        if features:
                            # emmigration - if it is too overcrowded
                            # the lions move to the first empty place
                            # else if there is no space the lion dies
                            if (area.count("L")>5) and (area.count("A")==0):
                                if (area.count(" ")>0):
                                    x = 0
                                    while x<3:
                                        y = 0
                                        while y<3:
                                            if grid.get(a+x,b+y) == " ":
                                                grid.set(a+x,b+y, lion(cell.Age))
                                                grid.set(a+1,b+1, " ")
                                                x = 4
                                                y = 4
                                            y+=1
                                        x+=1
                                    # since the lion has moved there is a chance
                                    # to die again
                                    if int(random()*32) == 1:
                                        grid.set(a+1, b+1, " ")
                                else:
                                    grid.set(a+1, b+1, " ")
                        else:
                            # overcrowding of lions
                            # if the conditions are met the lions dies
                            if (area.count("L")>5) and (area.count("A")==0):
                                grid.set(a+1, b+1, " ")
                # if it is still young and an antelope
                elif str(cell).upper() == "A":
                    # get the area
                    area = (grid.area(a, b)).upper()
                    # if the conditions are met the antelope is eaten
                    if (area.count("L")>4):
                        grid.set(a+1, b+1, " ")
                    # if the conditions are met the antelope is overcrowded
                    elif area.count("A") == 8:
                        grid.set(a+1,b+1, " ")
                    # running in feat mode
                    elif features:
                        # generate a random no, and if it equals 1 the antelope dies
                        # with a bigger chance than the lions, it seems more likely
                        if int(random()*20) == 1:
                            grid.set(a+1,b+1, " ")
            # cell is empty - check for procreation
            else:
                # get the surrounding area
                area = grid.area(a, b)
                if features:
                    # check if conditions apply for antelopes in feature mode
                    if (area.count("A")>1 and (area.count("a")+area.count("A"))>3 and (area.count("l")+area.count("L"))<4):
                        grid.set(a+1, b+1, antelope())
                    # check if conditions apply for lions
                    elif (area.count("L")>2 and (area.count("l")+area.count("L"))>3 and (area.count("a")+area.count("A"))<4):
                        grid.set(a+1, b+1, lion())
                #in non feature mode
                else:
                    if (area.count("A")>1 and (area.count("a")+area.count("A"))>3 and (area.count("l")+area.count("L"))<4):
                        grid.set(a+1, b+1, antelope())
                    # check if conditions apply for lions
                    elif (area.count("L")>2 and (area.count("l")+area.count("L"))>3 and (area.count("a")+area.count("A"))<4):
                        grid.set(a+1, b+1, lion())

    # Emmigration - reset edges so they do not influence they rest of the grid
    for a in range(grid.rows):
        grid.set(a, 0, " ")
        grid.set(a, -1, " ")

    for b in range (grid.columns+2):
        grid.set(0, b, " ")
        grid.set(-1, b, " ")

    if recordgrid:
        record(grid)

    # return the finished grid
    return grid
