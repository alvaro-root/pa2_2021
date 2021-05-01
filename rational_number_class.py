# simple Rational number class


class Rational:
    """ Implements a Rational number"""

    def __init__(self, numer, denom=1):  # note the default for "denom"
        print('in initializer')  # a "print" for illustration
        self.numer = numer
        self.denom = denom

    def __str__(self):
        """ String representation for printing"""
        print('in str')
        return str(self.numer) + '/' + str(self.denom)  # print as a fraction

    def __repr__(self):
        """ Representation of Rational number"""
        print('in repr')
        return f"{self.__class__.__name__}({self.numer}, {self.denom})"

    def __add__(self, f):
        """ Add two Rationals"""
        print('in add')
        if type(f) == int:  # convert ints to Rationals
            f = Rational(f)
        if type(f) == Rational:
            # find a common denominator (lcm)
            theLcm = __class__.lcm(self.denom, f.denom)
            # multiply to make denominators the same, then add numerators
            theSum = (theLcm / self.denom * self.numer) + \
                     (theLcm / f.denom * f.numer)
            return Rational(theSum, theLcm)
        else:
            print('wrong type')  # problem: some type we cannot handle
            raise (TypeError)

    def __radd__(self, f):
        """ Add two Rationals (reversed)"""
        # mapping is reversed: if "1 + x", x maps to self, and 1 maps to f
        print("in radd")
        # mapping is already reversed so self will be Rational; call __add__
        return self.__add__(f)

    def __iadd__(self, i):
        '''Increment'''
        print("in iadd")
        return self.__add__(i)

    def __sub__(self, f):
        """ Subtract two Rationals"""
        print('in sub')
        # subtraction is the same as addition with "+" changed to "-"
        theLcm = __class__.lcm(self.denom, f.denom)
        numeratorDiff = (theLcm / self.denom * self.numer) - \
                        (theLcm / f.denom * f.numer)
        return Rational(numeratorDiff, theLcm)

    def reduce_rational(self, rational):
        """ Return the reduced fractional value."""
        print('in reduce')
        # find the gcd and then divide numerator and denominator by gcd
        thegcd = __class__.gcd(rational.numer, rational.denom)
        return Rational(rational.numer / thegcd, rational.denom / thegcd)

    def __eq__(self, f):
        """ Compare two Rationals for equality"""
        print('in eq')
        # reduce both; then check that numerators and denominators are equal
        f1 = self.reduce_rational(self)
        f2 = f.reduce_rational(f)
        return f1.numer == f2.numer and f1.denom == f2.denom

    @staticmethod
    def gcd(a, b):
        # Ensure that a > b, if it is not reverse a & b
        if not a > b:
            a, b = b, a

        print(f"Initial fraction is {a}/{b}")
        while b != 0:
            rem = a % b
            a, b = b, rem
            print(f"... {a}/{b}")

        print(f"GCD is {a}")
        return a

    @staticmethod
    def lcm(a, b):
        print(f"LCM is {a * b // __class__.gcd(a, b)}")
        return (a * b // __class__.gcd(a, b))


if __name__ == "__main__":
    rat1 = Rational(1, 2)
    rat2 = Rational(3, 4)
    rat6 = Rational(6, 8)
    rat3 = rat1 + rat2
    rat4 = rat1.__add__(rat2)
    rat5 = Rational.__add__(rat1, rat2)
    rat7 = rat1 + 1
    print(f"rat7: {rat7}".format())

    print(rat1)
    print(rat2)

    print(rat2 == rat6)
