"""This module is an example for a while loop and if query to find a secret number

written during a VHS python course in Bochum.
Now I test the pydoc tool with this code

Author: Uwe Schweinsberg, Bochum
License: GNU GPL v 2
Date: 2. 9. 2019

functions: evaluate_number
"""


# import sys


def evaluate_number(n, sn):
    """evaluate_number compares two integers
    the first number is compared to the second.
    If the first number is smaller or bigger than the second number
    this information is printd. If the two numbers are equal there is no output.
    >>> evaluate_number(3, 5)
    Zu klein

    >>> evaluate_number(5, 3)
    Zu groß

    >>> evaluate_number(3, 3)

    ''
    """
    if n < sn:
        print("Zu klein")
    if n > sn:
        print("Zu groß")


# geheimnis = int(sys.argv[1])
geheimnis = 1052
versuch = 0
zaehler = 0
while versuch != geheimnis:
    versuch = int(input("Rate Zahl: "))
    evaluate_number(versuch, geheimnis)
    zaehler += 1
print("in ", zaehler, "Versuchen")

