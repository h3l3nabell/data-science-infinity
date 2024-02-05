# exception handling

try:
    age = int(input("Enter your age: "))
except:
    print("Invalid input. Please enter a number! ")

# some kinds of errors
# print(some_object)  # NameError

my_list = [1, 2]
my_list[4]  # IndexError

"5" + 6  # TypeError

int("Python")  # ValueError

3/0  # ZeroDivisionError

try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Invalid input - Please enter a number! ")

try:
    age = int(input("Enter your age: "))
    print(age)
except NameError:
    print("Invalid input - Please enter a number! ")


try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError as error_type:
    print(f"Invalid input - {error_type}. Please enter a number! ")
