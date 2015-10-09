from Animal import lion, antelope
from random import random

# a method to print the grid to the screen
def PrintGrid(grid, rows, cols):
    """A method to print the grid to the screen"""
    line = str()
    for a in range(rows):
        for b in range(cols):
            # add all the units in one string ("join" doesn't work with objects)
            line+=(str(grid[a+1][b+1])+"")
        line+="\n"

    #print the whole grid as one string
    print line

# a method to get the surrounding objects in one string for comparison with the centre object
def Area(grid, a, b):
    """A method to get the surrounding objects in one string for comparison with the centre object"""
    # get the object, throw it in a string and add it to the string
    ar = (str(grid[a][b])+str(grid[a][b+1])+str(grid[a][b+2])+str(grid[a+1][b])+
          str(grid[a+1][b+2])+str(grid[a+2][b])+str(grid[a+2][b+1])+str(grid[a+2][b+2]))
    return ar

# a method that runs the generations, given by "gen", or until a keyboard interrupt
def run (gen, grid, rows, cols):
    """A method that runs the generations, given by "gen", or until a keyboard interrupt"""
    # run it in a try block so it will catch the keyboard interrupt
    try:
        stopl = 0
        ext = False
        # the generation runs until "gen" (which will be -1 if it is undefined, so it will run indefinately)
        # and while there are animals in the grid
        while stopl!=gen and not ext:
            # animals that are too old are deleted
            for a in range(rows):
                for b in range(cols):
                    if grid[a+1][b+1]!=" ":
                        if grid[a+1][b+1].getAge()<0:
                            # just set their position to null
                            grid[a+1][b+1] = " "

            # procreation
            for a in range (rows):
                for b in range(cols):
                    # if an empty spot
                    if grid[a+1][b+1] == " ":
                        # get how the surrounding area is
                        area = Area(grid, a, b)
                        # check if conditions apply for antelopes
                        if (area.count("A")>2 and (area.count("a")+area.count("A"))>3 and (area.count("l")+area.count("L"))<4):
                            grid[a+1][b+1] = antelope()
                        # check if conditions apply for lions
                        elif (area.count("L")>2 and (area.count("l")+area.count("L"))>3 and (area.count("a")+area.count("A"))<4):
                            grid[a+1][b+1] = lion()

            # Emmigration - reset edges so they do not influence they rest of the grid
            for a in grid:
                a[0] = " "
                a[-1] = " "

            for b in range (cols+2):
                grid[0][b] = " "
                grid[-1][b] = " "
                
            # activities concerning lions
            for a in range(rows):
                for b in range(cols):
                    # if a lion
                    if str(grid[a+1][b+1]).upper() == "L":
                        #random deaths
                        # generate a random no, and if it equals 1 the lion dies
                        if int(random()*32) == 1:
                            grid[a+1][b+1] = " "
                    if str(grid[a+1][b+1]).upper() == "L":                
                        # overcrowding of lions
                        # get the area
                        area = (Area(grid, a, b)).upper()
                        # emmigration - if it is too overcrowded the lions move to the first empty place                        
                        # else if there is no space the lion dies
                        if (area.count("L")>5) and (area.count("A")==0):
                            if (area.count(" ")>0):
                                x = 0
                                while x<3:
                                    y = 0
                                    while y<3:
                                        if grid[a+x][b+y] == " ":
                                            grid[a+x][b+y] = lion(grid[a+1][b+1].Age)
                                            grid[a+1][b+1] = " "
                                            x = 4
                                            y = 4
                                        y+=1
                                    x+=1
                            else:
                                grid[a+1][b+1] = " "

            # activities concerning antelopes
            for a in range (rows):
                for b in range(cols):
                    # if an antelope
                    if str(grid[a+1][b+1]).upper() == "A":
                        #random deaths
                        # generate a random no, and if it equals 1 the antelope dies
                        # with a bigger chance than the lions, it seems more likely
                        if int(random()*20) == 1:
                            grid[a+1][b+1] = " "
                            
                        # get the area and convert to uppercase for easy comparison
                        area = (Area(grid, a, b)).upper()
                        # if the conditions are met the antelope is eaten
                        if (area.count("L")>4):
                            grid[a+1][b+1] = " "
                            
                        # if the conditions are met the antelope is overcrowded
                        if area.count("A") == 8:
                            grid[a+1][b+1] = " "

            # make each animal older
            for a in range(rows):
                for b in range(cols):
                    # if it is not an empty unit
                    if grid[a+1][b+1]!=" ":
                        grid[a+1][b+1].older()

            # check if all animals are dead
            ext = True
            for a in grid:
                for b in a:
                    if str(b).upper() != "":
                        ext = False
                    
            stopl+=1
            PrintGrid(grid, rows, cols)
    # if the user presses Ctrl+C the loop is stopped and the final no of generations are printed
    except (KeyboardInterrupt):
        PrintGrid(grid, rows, cols)
        print "No of generations: " +str(stopl)
    return grid
