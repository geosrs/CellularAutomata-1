from Tkinter import *
from ttk import *
import Generation
import tkMessageBox
from caframe import caframe
from cagrid import cagrid
import checkbox

def PrintGrid(grid):
    """ A method to print the grid to the screen
    """
    # clear the grid/canvas
    anigrid.delete(ALL)
    images = {'L': PhotoImage(file="img/lion.gif"),
                'l': PhotoImage(file="img/young_lion.gif"),
                'A': PhotoImage(file="img/antelope.gif"),
                'a': PhotoImage(file="img/young_antelope.gif"),
                ' ': None}
    a = 0
    for row in grid.grid:
        b = 0
        # skip the empty first row
        if a>0:
            for animal in row:
                if b>0:
                    # get the image depending on the cell
                    cellimage = images[str(animal)]

                    anigrid.create_image((b-0.8)*20.0,
                                        (a-0.8)*20.0,
                                        anchor=NW,
                                        image = cellimage)
                b+=1
        a+=1
    # update the canvas to make it display the new grid
    anigrid.update()

# run the simulation from the file
def runrecording():
    # reset the checkboxes
    inframe.reset()
    anigrid.delete(ALL)
    recd = open("record.txt")
    ngrid = []
    # get the rows and columns from the first line
    layout = recd.readline().split(" ")
    rows = int(layout[0])
    cols = int(layout[1])

    for line in recd:
        # decode the line
        decode = ""
        for a in line:
            if a.isdigit():
                space = " "*int(a)
                decode+=space
            else:
                decode+=a

        ngrid = cagrid(rows, cols, 0, 0 ,0 , decode)
        anigrid.after(100, PrintGrid(ngrid))

        if inframe.interrupt():
            break

    recd.close()


def finished(grid):
    """ Finish the run and print out the data
    """
    lions = 0
    ants = 0
    for row in range(grid.rows):
        for col in range(grid.columns):
            if str(grid.get(row,col)).upper() == "L":
                lions+=1
            elif str(grid.get(row,col)).upper() == "A":
                ants+=1

    tkMessageBox.showinfo(title = "Finished",
                    message = "  Lions: "+str(lions)+"\n Antelopes: "+str(ants))

def firstRecording(grid):
    """ Record the first iteration of the grid
    """
    temp = open("record.txt", 'w')
    temp.write(str(grid.rows) + " " + str(grid.columns) + "\n")
    temp.close()

    line = ""
    for a in range(1, grid.rows+1):
        for b in range(1, grid.columns+1):
            # add all the units in one string
            line+=(str(grid.get(a, b)))

    cline = ""
    no = 0
    for a in line:
        if " " == a:
            no+=1
        elif no!=0:
            cline+=(str(no)+a)
            no = 0
        else:
            cline+=a
    if no!=0:
        cline+=(str(no))
    recfl = open ("record.txt", 'a')
    recfl.write(cline+"\n")

    recfl.close()

def startrun():
    """ Start the simulation
    """
    # catch errors
    try:
        inframe.reset()
        # set grid size, get the values from the entry boxes
        # reset the checkboxes
        rows = int(inframe.rows())
        cols = int(inframe.columns())
        empty = float(inframe.empty())
        lions = float(inframe.lions())
        antelopes = float(inframe.antelopes())
        grid = cagrid(rows, cols, empty, lions, antelopes, False)

        # enter how many generations it should run, if nothing is entered
        # gen stays -1 and the generations loop runs indefinately
        gen = -1
        run = inframe.generations()
        if run:
            gen = int(run)

        # print the initial grid
        PrintGrid(grid)
        # record the initial grid
        firstRecording(grid)

        # run the generation
        stop = 0
        ext = False
        # the generation runs until "gen" or indefinately
        # and while the user has not pressed stop
        while stop!=gen and not ext:
            grid = Generation.run(grid, inframe.features(), inframe.recording())

            # the canvas is only changed after a period of time
            anigrid.after(100, PrintGrid(grid))

            # increment the loop counter
            stop+=1
            # check whether the stop button has been pressed
            ext = inframe.interrupt()

        finished(grid)
    # display an error message box
    except ValueError:
        tkMessageBox.showerror(title = "Error",
                                message = "Please enter only numbers")
    except IndexError:
        tkMessageBox.showerror(title = "Error",
                                message = "Please enter positive numbers")
    except TclError:
         pass
    except:
        tkMessageBox.showerror(title = "Error",
                                message = "Unknown error:\nPlease try again")

def exitsim():
    """ close the window
    """
    root.destroy()

if __name__ == "__main__":
    # build the GUI window here
    # main frame
    root = Tk()
    root.title("CellularAutomata")

    # style it
    style = Style()
    style.theme_use('clam')

    features = checkbox.checkbox()

    # make an interface frame
    inframe = caframe(root,
                    startrun,
                    runrecording,
                    exitsim)

    # define canvas
    anigrid = Canvas(root,
                    height = 900,
                    width = 1200,
                    bg = "white",
                    confine = False,
                    bd = 3,
                    relief = "sunken")

    # put the frame and the canvas in the root
    inframe.grid (row = 0, column = 0, sticky = N)
    anigrid.grid (row = 0, column = 1)

    #run it
    root.mainloop()
