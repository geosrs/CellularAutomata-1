from Tkinter import *
from ttk import *
import tkMessageBox
from checkbox import checkbox

class caframe(Frame):
    """ Builds a tkinter window for the cellular automata
    """

    def __init__(self, parent, startrun, runrecording, exit):
        Frame.__init__(self, parent)

        self.rec = checkbox()
        self.feat = checkbox()
        self.inter = checkbox()

        # register the validation command
        vcmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # define size of the grid labels/entry boxes
        self.sizelabel = Label(self, text = "Size:")
        self.rowlabel = Label(self, text = "Rows:")
        self.collabel = Label(self, text = "Columns:")
        self.rowent = Entry(self, width = 10, validate = 'focusout', validatecommand = vcmd)
        self.colent = Entry(self, width = 10)

        # define ratios labels/entry boxes
        self.ratlabel = Label(self, text = "Ratio:")
        self.emptlabel = Label(self, text = "Empty:")
        self.lionlabel = Label(self, text = "Lions:")
        self.antlabel = Label(self, text = "Antelope:")
        self.emptent = Entry(self, width = 10)
        self.lionent = Entry(self, width = 10)
        self.antent = Entry(self, width = 10)

        # define running time labels/entry boxes
        self.runlabel = Label(self, text = "Running Time:")
        self.genlabel = Label(self, text = "Generations:")
        self.genent = Entry(self, width = 10)

        # define buttons
        # the stop button sets the state of the interrupt object to false
        # so that the generation loop stops
        self.stopb = Button(self, text = "Stop", command = self.inter.pressed)
        self.runb = Button(self, text = "Run", command = startrun)
        self.exitb = Button(self, text = "Exit", command = exit)

        self.recrd = Checkbutton(self, text="Record simulation", command=self.rec.pressed)
        self.run = Button (self, text = "Run Recording", command = runrecording)
        self.featr = Checkbutton(self, text="Run with features", command=self.feat.pressed)

        #put the widgets in the frame
        self.sizelabel.grid(row = 0, column = 0, sticky=W)
        self.rowlabel.grid(row = 1, column = 0,sticky=E)
        self.rowent.grid(row = 1, column = 1)
        self.collabel.grid(row = 2, column = 0,sticky=E)
        self.colent.grid(row = 2, column = 1)

        self.ratlabel.grid(row = 3, column = 0, sticky=W)
        self.emptlabel.grid(row = 4, column = 0,sticky=E)
        self.emptent.grid(row = 4, column = 1)
        self.lionlabel.grid(row = 5, column = 0,sticky=E)
        self.lionent.grid(row = 5, column = 1)
        self.antlabel.grid(row = 6, column = 0,sticky=E)
        self.antent.grid(row = 6, column = 1)

        self.runlabel.grid(row = 7, column = 0, sticky=W)
        self.genlabel.grid(row = 8, column = 0, sticky=E)
        self.genent.grid(row = 8, column = 1)

        self.featr.grid(row = 9, column = 0, columnspan = 2)
        self.recrd.grid(row = 10, column = 0, columnspan = 2)

        self.runb.grid(row = 12, column = 0, columnspan=2, sticky = N+E+S+W)
        self.stopb.grid(row = 13, column = 0, columnspan=2, sticky = N+E+S+W)
        self.run.grid(row = 14, column = 0, columnspan = 2, sticky = N+E+S+W)
        self.exitb.grid(row = 15, column = 0, columnspan = 2, sticky = N+E+S+W)

    def onValidate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789.+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def columns(self):
        """ Returns the columns entered
        """
        return self.colent.get()

    def rows(self):
        """ Returns the rows entered
        """
        return self.rowent.get()

    def empty(self):
        """ Returns the empty entered
        """
        return self.emptent.get()

    def lions(self):
        """ Returns the lions entered
        """
        return self.lionent.get()

    def antelopes(self):
        """ Returns the antelopes entered
        """
        return self.antent.get()

    def generations(self):
        """ Returns the generations entered
        """
        return self.genent.get()

    def record(self):
        """ Return the recording state
        """
        return self.rec.state

    def features(self):
        """ Return the features state
        """
        return self.feat.state

    def interrupt(self):
        """ Return the interrupt state
        """
        return self.inter.state

    def reset(self):
        """ Reset the checkboxes
        """
        self.rec.state = False
        self.feat.state = False
        self.inter.state = False
