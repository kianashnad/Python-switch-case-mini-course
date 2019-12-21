def bravo():
    print("Here is bravo 1-1")

def charlie():
    print("Here is charlie 1-1")

def deeeeefult():
    print("deeeeeeeeeeeefault")

switcher = {
    0: bravo,
    1: charlie
}

def exec_by_number(argument):
    func = switcher.get(argument, deeeeefult)
    return func()

exec_by_number(2)