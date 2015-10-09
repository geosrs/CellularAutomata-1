from Animal import lion, antelope
from random import random
from threading import Timer
from Tkinter import *
import Interrupt
import tkMessageBox

def finished(grid):
    lions = 0
    ants =0
    for a in grid:
        for b in a:
            if str(b).upper() == "L":
                lions+=1

    for a in grid:
        for b in a:
            if str(b).upper() == "A":
                ants+=1

    tkMessageBox.showinfo(title = "Finished", message = "  Lions: "+str(lions)+"\n Antelopes: "+str(ants))


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
    for a in range(len(grid)-1):
        for b in range(len(grid[a])-1):
            # add all the units in one string ("join" doesn't work with objects)
            line+=(str(grid[a+1][b+1]))

    line = compress(line)
    recfl = open ("record.txt", 'a')
    recfl.write(line+"\n")

    recfl.close()


# a method to print the grid to the screen
def PrintGrid(grid, rows, cols, anigrid):
    """A method to print the grid to the screen"""
    # clear the grid
    anigrid.delete(ALL)
    for a in range(rows):
        for b in range(cols):
            # add all the units to the canvas
            anigrid.create_text(a*11, b*11, text = str(grid[a+1][b+1]))
    # update the canvas to make it display the new grid
    anigrid.update()
    
# a method to get the surrounding objects in one string for comparison with the centre object
def Area(grid, a, b):
    """A method to get the surrounding objects in one string for comparison with the centre object"""
    # get the object, throw it in a string and add it to the string
    ar = (str(grid[a][b])+str(grid[a][b+1])+str(grid[a][b+2])+str(grid[a+1][b])+
          str(grid[a+1][b+2])+str(grid[a+2][b])+str(grid[a+2][b+1])+str(grid[a+2][b+2]))
    return ar


# a method to run the generations, given by "gen", or until a keyboard interrupt
def run(gen, grid, rows, cols, anigrid, inter, rec, feat):
    """A method that runs the generations, given by "gen", or until a the user presses stop"""
    stopl = 0
    ext = False
    # the generation runs until "gen" (which will be -1 if it is undefined, so it will run indefinately)
    # and while the user has not pressed stop
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
                    if feat.getState():
                        # check if conditions apply for antelopes in feature mode
                        if (area.count("A")>1 and (area.count("a")+area.count("A"))>3 and (area.count("l")+area.count("L"))<4):
                            grid[a+1][b+1] = antelope()
                        # check if conditions apply for lions
                        elif (area.count("L")>2 and (area.count("l")+area.count("L"))>3 and (area.count("a")+area.count("A"))<4):
                            grid[a+1][b+1] = lion()
                    #in non feature mode
                    else:
                        if (area.count("A")>1 and (area.count("a")+area.count("A"))>3 and (area.count("l")+area.count("L"))<4):
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
                    if feat.getState():
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
                    else:   
                        # overcrowding of lions
                        # get the area
                        area = (Area(grid, a, b)).upper()
                        # if the conditions are met the lions dies
                        if (area.count("L")>5) and (area.count("A")==0):
                            grid[a+1][b+1] = " "

        # activities concerning antelopes
        for a in range (rows):
            for b in range(cols):
                # if an antelope
                if str(grid[a+1][b+1]).upper() == "A":
                    # get the area and convert to uppercase for easy comparison
                    area = (Area(grid, a, b)).upper()
                    # if the conditions are met the antelope is eaten
                    if (area.count("L")>4):
                        grid[a+1][b+1] = " "
                        
                    # if the conditions are met the antelope is overcrowded
                    if area.count("A") == 8:
                        grid[a+1][b+1] = " "
                # running in feat mode
                if feat.getState():
                    if str(grid[a+1][b+1]).upper() == "A":
                        # generate a random no, and if it equals 1 the antelope dies
                        # with a bigger chance than the lions, it seems more likely
                        if int(random()*20) == 1:
                            grid[a+1][b+1] = " "

        # make each animal older
        for a in range(rows):
            for b in range(cols):
                # if it is not an empty unit
                if grid[a+1][b+1]!=" ":
                    grid[a+1][b+1].older()              
        # the canvas is only changed after a period of time
        anigrid.after(200, PrintGrid(grid, rows, cols, anigrid) )

        # increment the loop counter
        stopl+=1
        if rec.getState():
            record(grid)
        # check whether the stop button has been pressed
        ext = inter.getState()
    # return the finished grid
    finished(grid)
    return grid
