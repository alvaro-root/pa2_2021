"""
A closure is a function and an extended scope that contains free variables. By definition, a closure is a nested
function that references one or more variables from its enclosing scope.

MF Jan 2021
"""

def say():
    """
    In Python, you can define a function from the inside of another function. And this function is called a nested
    function.

    In this example, we define the display function inside the say function. The display function is called a nested
    function. Inside the display function, you access the greeting variable from its nonlocal scope. Python calls the
    greeting variable as a free variable.

    When you look at the display function, you actually look at:
    * The display function itself.
    * And the free variable greeting with the value 'Hello'.

    So the combination of the display function and greeting variable is called a closure.

    RETURNING AN INNER FUNCTION:
    In this example, the say function returns the display function instead of executing it. Also, when the say function
    returns the display function, it actually returns the closure.


    """
    greeting = 'Hello'
    print(f"id(greeting) Outer scope -> {hex(id(greeting))}")

    def display():
        print(f"id(greeting) Inner scope -> {hex(id(greeting))}")
        print(f"Greeting is: {greeting}")

    return display

if __name__ == '__main__':
    # The following assigns the return value of the say function to a variable fn. Since fn is a function, you can
    # execute it.

    # The say function executes and returns a function. When the fn function executes, the say function already completes.
    # In other words, the scope of the say function was gone at the time the fn function executes. Since the greeting
    # variable belongs to the scope of the say function, it should also be destroyed with the scope of the function.
    # However, you still see that fn displays the value of the message variable.

    fn = say()
    fn()

    # Python cells and multi-scoped variables
    # The value of the message variable is shared between two scopes of:
    # * The say function.
    # * The closure
    #
    # The label message is in two different scopes. However, they always reference the same string object with the value
    # 'Hello'. To achieve this, Python creates an intermediary object called a cell. To find the memory address of the
    # cell object, you can use the __closure__ property as follows.

    print(f"Closure: {fn.__closure__}")
    print(f"fn.__closure__[0].cell_contents -> {fn.__closure__[0].cell_contents}")

    # The __closure__ returns a tuple of cells. In this example, the memory address of the cell is 0x0000017184915C40.
    # It references a string object at 0x0000017186A829B0.
    #
    # If you display the memory address of the string object in the say function and closure, you should see that they
    # reference the same object in the memory.
    #
    # When you access the value of the greeting variable, Python will technically “double-hop” to get the string value.
    # This explains why when the say() function was out of scope, you still can access the string object referenced by the
    # greeting variable.
    #
    # Based on this mechanism, you can think of a closure as a function and an extended scope that contains free variables.
    # To find the free variables that a closure contains, you can use the __code__.co_freevars.
    
    print(f"fn.__code__.co_freevars -> {fn.__code__.co_freevars}")
