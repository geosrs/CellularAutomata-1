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

    
    def __str__(self):
        """Returns a string-representation of the antelope
            as an adult or baby"""
        if self.Adult:
            #adult is capital A
            return "A"
        else:
            #baby is small a
            return "a"

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

    def __str__(self):
        """Returns a string-representation of the lion
            as an adult or baby"""
        if self.Adult:
            return "L"
        else:
            return "l"
