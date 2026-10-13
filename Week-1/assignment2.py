"""
Assignment 2 - List, Tuple, Dictionary, Set and IF-conditions.

Every task is a small function. Only the last task (IF-Condition #5) is run
by default - add or remove tasks in TASKS_TO_RUN to execute others.
"""


# ---------------------------- Data structures ----------------------------

def list_sum():
    numbers = [5, 10, 15, 20]
    print(sum(numbers))


def list_maximum():
    numbers = [12, 45, 7, 23, 89]
    print("The largest number is", max(numbers))


def tuple_count():
    numbers = (2, 4, 2, 6, 2, 8)
    print("Number of time 2 appears is ", numbers.count(2))


def dictionary_marks():
    marks = {"English": 75, "Math": 85, "Python": 90}
    marks["English"] = 90
    print(marks)
    for subject in marks:
        print(subject)


def set_difference():
    print({1, 2, 3, 4}.difference({3, 4, 5, 6}))


# ------------------------------ IF-conditions ------------------------------

def positive_or_negative():
    num = float(input("Enter a nmumber: "))
    print("Number is positive" if num > 0 else "Number is Negative")


def even_or_odd():
    num = int(input("Enter a Nmumber: "))
    print("The number is Even" if num % 2 == 0 else "The number is Odd")


def voting_eligibility():
    age = float(input("Enter ypur age: "))
    print("You are eligible to vote" if age >= 18 else "You are not eligible to vote")


def temperature_check():
    temp = float(input("Enter temperature: "))
    print("It is hot today." if temp > 30 else "Weather is Normal today")


def greater_number():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num1 > num2:
        print("First number is greater.")
    elif num2 > num1:
        print("Second number is greater.")
    else:
        print("Both are equal.")


TASKS_TO_RUN = [greater_number]

if __name__ == "__main__":
    for task in TASKS_TO_RUN:
        task()
