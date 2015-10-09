# a class that changes it's state when it is "pressed"
class rec:
    # initiate the object with a false state
    def __init__(self):
        """Makes a new interrupt object with a default state of False"""
        self.state = False

    # when it is pressed it changes to true
    def pressed(self):
        """changes the state to True"""
        self.state = True != self.state

    # returns the state
    def getState(self):
        return self.state
