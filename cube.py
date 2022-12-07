# exercise 1
def cube(num):
    """Return the cube of the input number."""
    cube_num = pow(num, 3)
    return cube_num


print(f"0 cubed is {cube(0)}")
print(f"2 cubed is {cube(2)}")

# exercise 2


def greet(name): 
    """Display a greeting."""
    print(f"Hello {name}!")


greet("Guido")
