from Animal import lion, antelope
from random import random

class cagrid:

    def __init__(self, rows, cols, empty, lions, antelopes, recording):
        """ A method to initiate the grid with lions and antelopes
        """

        self.grid = []
        self.rows = rows
        self.columns = cols

        # this is not a recording
        if not recording:
            # calculate the total number animals to be in the grid
            totrat = empty+lions+antelopes

            # iterate through the cells
            # +2 edge for emmigration
            for row in range(rows+2):
                self.grid.append(list(" "*(cols+2)))
                for col in range(cols+2):
                    # random number in the total range
                    num = random()*totrat
                    # check which item is assigned to the cell
                    if num > empty:
                        if num <= empty + lions:
                            self.grid[row][col] = lion()
                        else:
                            self.grid[row][col] = antelope()
        # rebuild from a recording
        else:
            i=0
            rw = [' ']
            self.grid.append(list(' '*(cols+1)))
            # iterate through each char in the recorded line
            for a in recording:
                rw.append(a)
                i+=1
                # at the end of a column go to next row
                if i == (cols-1):
                    self.grid.append(rw)
                    rw=[' ']
                    i=0


    def get(self, row, column):
        """ Return the cell at specific coordinates
        """
        return self.grid[row][column]

    def set(self, row, column, value):
        """ Set the value for a specific cell
        """
        self.grid[row][column] = value

    def area(self, a, b):
        """ Get the surrounding objects in one string
            for comparison with the centre object
        """
        # adjust so to count from the corner
        a-=1
        b-=1
        # get the object, throw it in a string and add it to the string
        return (str(self.grid[a][b])+
                str(self.grid[a][b+1])+
                str(self.grid[a][b+2])+
                str(self.grid[a+1][b])+
                str(self.grid[a+1][b+2])+
                str(self.grid[a+2][b])+
                str(self.grid[a+2][b+1])+
                str(self.grid[a+2][b+2]))

    def age(self, a, b):
        """ If the cell is an animal, age it
        """
        self.grid[a][b].older()
