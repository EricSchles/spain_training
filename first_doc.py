from functools import partial

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix        
def adder(a: int, b: int) -> int:
    """
    # Description:
    -------------
    This function helps to sum 2 int numbers

    # Inputs:
    -------------
    * a : float - The first parameter to sum
    * b : float - The second parameter to sum.
    
    # Output
    -------------
    The sum of both numbers a and b. which is an int.
    """
    return a+b