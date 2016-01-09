# the antelope class
class antelope:
    # define a new antelope with default age 1
    def __init__(self, age = 1):
        """Create a new antelope"""
        self.Adult = False
        self.Age = age

    def older(self):
        """Increment the age with one"""
        self.Age+=1

        # if the antelope is old enough it becomes an adult
        if self.Age>1:
            self.Adult = True
        if self.Age == 10:
            self.Age = -2

    def getAge(self):
        """Get the age"""
        return self.Age

    def compare(self):
        """ return integer representation of the antelope """
        if self.Adult:
            return 2
        return 1

    def __str__(self):
        """ Returns a representation of the antelope
            as an adult or baby. 1 for baby, 9 for adult
        """
        if self.Adult:
            #adult is 9
            return '2'
        #baby is 1
        return '1'

    def __cmp__(self, other):
        if self.Adult:
            return cmp(2, other)
        return cmp(1, other)

    def __add__(self, other):
        if self.Adult:
            return 2 + other
        return 1 + other

# the lion class
class lion:
    # create a new lion with default age 1
    def __init__(self, age = 1):
        """Create a new lion"""
        self.Adult = False
        self.Age = age

    def older(self):
        """Increment the age with 1"""
        self.Age+=1

        # if the lion is old enough it becomes an adult
        if self.Age>2:
            self.Adult = True
        if self.Age == 21:
            self.Age = -2

    def getAge(self):
        """Get the age"""
        return self.Age

    def compare(self):
        """ return integer representation of the lion """
        if self.Adult:
            return 4
        return 3

    def __str__(self):
        """ Returns a string-representation of the lion
            as an adult or baby. 3 for baby, 4 for adult.
        """
        if self.Adult:
            return '4'
        return '3'

    def __cmp__(self, other):
        if self.Adult:
            return cmp(4, other)
        return cmp(3, other)
