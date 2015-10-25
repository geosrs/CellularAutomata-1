class checkbox(object):
    """ A class that changes it's state when it is "pressed"
    """

    def __init__(self):
        """Makes a new interrupt object with a default state of False
        """
        self.state = False

    # when it is pressed it changes to true
    def pressed(self):
        """ Toggle the checkbox state
        """
        self.state = not self.state
