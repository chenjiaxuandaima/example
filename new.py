def add(a,b):
    try:
        return a+b
    except:
        raise TypeError
def multiply(a,b):
    try:
        return a*b
    except:
        raise TypeError
def sub(a,b):
    try:
        return a-b
    except:
        raise TypeError
def divide(a,b):
    try:
        return a/b
    except:
        raise TypeError
<<<<<<< HEAD
def power(a,b):
    assert type(b) is int
    if b==1:
        return a
    else:
        return a*power(a,b-1)
=======
def factorial(a):
    assert type(a) is int
    if a==1:
        return a
    else:
        return a*factorial(a-1)S
>>>>>>> beta_A
