def complexfunc1(n: float):
    """check number size"""
    if n < 0:
        return "negative"
    elif n < 100:
        return "ok"
    else:
        return "very big"
