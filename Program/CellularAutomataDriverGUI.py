from Animal import lion, antelope
from random import random
from Tkinter import *
import Generation
import tkMessageBox
import Interrupt
import Record

# a method to print the grid to the screen
def PrintGrid(grid, rows, cols):
    """A method to print the grid to the screen"""
    # clear the grid/canvas
    anigrid.delete(ALL)
    for a in range(rows):
        for b in range(cols):
            # add all the units in list to the canvas
            anigrid.create_text(a*11, b*11, text = str(grid[a+1][b+1]))

        
# a method to initiate the grid with lions and antelopes
def newGrid (grid, rows, cols):
    """A method to initiate the grid with lions and antelopes"""

    # make an empty grid, empty being " ", with one extra line on each edge
    # so it is easier to check the area of each animal
    grid = []
    for a in range (rows+2):
        grid.append(list(" "*(cols+2)))
    
    # get the seperate ratios
    empt = float(emptent.get())
    ln = float(lionent.get())
    ant = float(antent.get())

    # calculate the total no animals to be in the grid
    totrat = empt+ln+ant
    totspace = float(rows*cols)
    mul = totspace/totrat
    lions = int(mul*ln)
    antes = int(mul*ant)
    
    # enter the lions
    for a in range(lions):
        # generate random indexes
        rind = int(random()*rows)+1
        cind = int(random()*cols)+1
        # make sure the spot is empty
        if grid[rind][cind] != " ":
            rind = int(random()*rows)+1
            cind = int(random()*cols)+1
            # run until an empty spot is found
            while str(grid[rind][cind]) != " ":
                rind = int(random()*rows)+1
                cind = int(random()*cols)+1
                
            grid[rind][cind] = lion()
            
        else:
            grid[rind][cind] = lion()

    # enter the antelopes
    for a in range(antes):
        rind = int(random()*rows)+1
        cind = int(random()*cols)+1

        # make sure the spot is empty
        if grid[rind][cind] != " ":
            rind = int(random()*rows)+1
            cind = int(random()*cols)+1

            while str(grid[rind][cind]) != " ":
                rind = int(random()*rows)+1
                cind = int(random()*cols)+1
                
            grid[rind][cind] = antelope()
            
        else:
            grid[rind][cind] = antelope()

    return grid

# a method to print the recorded grid to the screen
def PrintRec(grid, rows, cols):
    """A method to print the grid to the screen"""
    # clear the grid/canvas
    anigrid.delete(ALL)
    for a in range(rows):
        for b in range(cols):
            # add all the units in list to the canvas
            anigrid.create_text(a*11, b*11, text = str(grid[a][b]))


# run the simulation from the file
def runsim():
    anigrid.delete(ALL)
    recd = open("record.txt")
    ngrid = []
    rows = int(rowent.get())
    cols = int(colent.get())
    for line in recd:
        ngrid = makeGrid(decode(line), rows)
        anigrid.after(200, PrintRec(ngrid, rows, cols))


# decode the line in the file
def decode(line):
    dcd = ""
    print line
    for a in line:
        if a.isdigit():
            space = " "*int(a)
            dcd+=space
        else:
            dcd+=a
    print len(dcd)
    return dcd

# make a new grid from the decoded line
def makeGrid(gridln, rows):
    grid = []
    rw = []
    for a in gridln:
        for i in range(rows):
            rw.append(a)
        grid.append(rw)
        rw = []

    return grid

    
def main():
    """This method co-ordinates the main methods for the actual grid"""
    # catch errors
    try:      
        # set grid size, get the values from the entry boxes
        rows = int(rowent.get())
        cols = int(colent.get())
        grid = []
        grid = newGrid(grid, rows, cols)
            
        # enter how many genrations it should run, if nothing is entered
        # gen stays -1 and the generations loop runs indefinately
        gen = -1
        run = genent.get()
        if run:
            gen = int(run)
            
        # print the initial grid
        PrintGrid(grid, rows, cols)

        temp = open("record.txt", 'w')
        temp.write("")
        temp.close()
        
        # run the generation  
        grid = Generation.run(gen, grid, rows, cols, anigrid, inter, rec, feat)
    # display an error message box
    except ValueError:
        tkMessageBox.showerror(title = "Error", message = "Please enter only numbers")
    except IndexError:
        tkMessageBox.showerror(title = "Error", message = "Please enter positive numbers")
    except TclError:
         pass
    except:
        tkMessageBox.showerror(title = "Error", message = "Unknown error:\nPlease try again")
        
if __name__ == "__main__":
    # create a new interrupt object to stop the loop
    inter = Interrupt.interrupt()
    rec = Record.rec()
    feat = Record.rec()
    """Build the GUI window"""
    # build the GUI window here
    # main frame
    root = Tk()
    root.title("CellularAutomata")

    # make an interface frame
    inframe = Frame(root)

    # define size of the grid labels/entry boxes
    sizelabel = Label(inframe, text = "Size:")
    rowlabel = Label(inframe, text = "Rows:")
    collabel = Label(inframe, text = "Columns:")
    rowent = Entry(inframe, width = 10)
    colent = Entry(inframe, width = 10)

    # define ratios labels/entry boxes
    ratlabel = Label(inframe, text = "Ratio:")
    emptlabel = Label(inframe, text = "Empty:")
    lionlabel = Label(inframe, text = "Lions:")
    antlabel = Label(inframe, text = "Antelope:")
    emptent = Entry(inframe, width = 10)
    lionent = Entry(inframe, width = 10)
    antent = Entry(inframe, width = 10)

    # define running time labels/entry boxes
    runlabel = Label(inframe, text = "Running Time:")
    genlabel = Label(inframe, text = "Generations:")
    genent = Entry(inframe, width = 10)
    x = 4
    # define canvas
    anigrid = Canvas(root, height = 700, width = 900, bg = "white", confine = False, bd = 3, relief = "sunken")
    # define buttons
    # the stop button sets the state of the interrupt object to false so that the generation loop stops
    stopb = Button(inframe, text = "Stop", command = inter.pressed)
    runb = Button(inframe, text = "Run", command = main)

    recrd = Checkbutton (inframe, text = "Record Simulation", command = rec.pressed)
    run = Button (inframe, text = "Run Recording", command = runsim)
    featr = Checkbutton (inframe, text = "Run with features", command = feat.pressed)

    #put the widgets in the frame
    sizelabel.grid(row = 0, column = 0, columnspan = 2)
    rowlabel.grid(row = 1, column = 0)
    rowent.grid(row = 1, column = 1)
    collabel.grid(row = 2, column = 0)
    colent.grid(row = 2, column = 1)

    ratlabel.grid(row = 3, column = 0, columnspan = 2)
    emptlabel.grid(row = 4, column = 0)
    emptent.grid(row = 4, column = 1)
    lionlabel.grid(row = 5, column = 0)
    lionent.grid(row = 5, column = 1)
    antlabel.grid(row = 6, column = 0)
    antent.grid(row = 6, column = 1)

    runlabel.grid(row = 7, column = 0, columnspan = 2)
    genlabel.grid(row = 8, column = 0)
    genent.grid(row = 8, column = 1)

    stopb.grid(row = 9, column = 0, sticky = N+E+S+W)
    runb.grid(row = 9, column = 1, sticky = N+E+S+W) 

    recrd.grid(row = 10, column = 0, columnspan = 2)
    run.grid(row = 11, column = 0, columnspan = 2)
    featr.grid(row = 12, column = 0, columnspan = 2)

    # put the frame and the canvas in the root
    inframe.grid (row = 0, column = 0, sticky = N)
    anigrid.grid (row = 0, column = 1)

    #run it
    root.mainloop()
