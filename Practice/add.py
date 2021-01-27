def outer():
    x=3
    def inner():
        print(x**3)
    return inner
foo=outer()
foo()