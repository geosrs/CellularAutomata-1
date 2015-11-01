class checkbox(object):
    """ A class that changes it's state when it is "pressed"
    """

    def __init__(self):
        """Makes a new interrupt object with a default state of False
        """
        self.state = False

    def pressed(self):
        """ Toggle the checkbox state
        """
        self.state = not self.state

    def getState(self):
        """ Return the state
        """
        return self.state

    def reset(self):
        """ Reset the state to false
        """
        self.state = False
