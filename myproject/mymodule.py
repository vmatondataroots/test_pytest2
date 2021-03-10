def func1(x):
    """some doc"""
    return x + 1

def mygreetings(name: str):
    """some doc 2"""
    return f"Hello {name}"

def myfunc1(x: float) -> float:
    """returns sum of list"""
    return sum(x)

def myfunc2(l: list) -> int:
    """returns len of list"""
    return len(l)

print("----------- mymodule executed --------------")
