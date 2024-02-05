"""
  Functions
"""

# Version 1


def happy_birthday():
    print("Happy Birthday!")


happy_birthday()


# Version 2


def happy_birthday(name):
    print(f"Happy Birthday {name}!")


happy_birthday("Mary")


# Version 3


def happy_birthday(name="To You"):
    print(f"Happy Birthday {name}!")


happy_birthday("Mary")
happy_birthday()
