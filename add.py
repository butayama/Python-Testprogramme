"""Modul mit add-Funktion"""

def demo_add(a, b):
    # Addition zweier Zahlen
    """
    >>> res = demo_add(3, 5)
    >>> res
    8
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()