# This is an example of a function that takes any number of positional arguments
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2, 3, 4, 5))
print(avg(1, 2, 2, 2, 1))

# This is an example of a function that takes any number keyword arguments
def make_element(name, value, **attrs):
    keyvals = ['%s=


