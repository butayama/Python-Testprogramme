"""Example Doctest source: Hubertz, J. Softwaretests mit Python 2.6.4 S.46

Examples for doctest: Ausnahmebehandlung (structured exception handling, abbr. SEH)
and direct call with __main__

Author: Uwe Schweinsberg, Bochum
License: GNU GPL v 2
Date: 2. 9. 2019

functions: ausnahme_check
"""

def ausnahme_check():
    """ausnahme_check verursacht eine Ausnahme, der Test
    soll zeigen, dass dies tatsächlich geschieht.
    >>> c = ausnahme_check()
    Traceback (most recent call last):
    RuntimeError: Ausnahme
    """
    raise RuntimeError('Ausnahme')


if __name__ == "__main__":
    import doctest
    doctest.testmod()