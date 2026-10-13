# Function and return values
# def add_numbers(a, b):
#     result = a + b 
#     return result

# total = add_numbers(5, 3)
# print(total)

# def square(x):
#     squ = x**2
#     return squ

# print(square(2))
# print(square(3))
# print(square(10))

# print("--------------------------------")

# def greet(name):
#     return f"Hello, {name}"
    
# print(greet("Ali!"))

# print("--------------------------------")

# def greet(name):
#     greeting = f"Hello, {name}"
#     return greeting

# print(greet("Ali!"))

# print("------------------------------")

# def square(n):
#     squ = n * n
#     return squ

# user_squ = int(input("Enter the number: "))
# print(square(user_squ))

# print("--------------------------------")

# def greet(name):
#     return f"Hello, {name}"

# user_name = input("Enter your name: ")
# print(greet(user_name))

# print("------------------------------")

# # Function Scope
# x = 10
# def my_funct():
#     y = 5
#     print(x + y)

# my_funct()

# print("---------------------------")

# x = 11
# def my_func():
#     b = 15
#     print(x)
#     print(b)

# my_func()

# print(b)

# Lambda Function

# square = lambda x: x * x
# print(square(5))

# print("-----------------------")
 
# add = lambda a, b: a + b
# print(add(3, 4))


# print("--------------------")

# multiple = lambda a, b: a * b
# print(multiple(5, 4))
# print(multiple(4, 3))

# print("-----------------")

# num = lambda x: x % 2 == 0
# print(num(15)) 

# # Map And Filter

# nums = [1, 2, 3, 4, 5]

# squared = list(map(lambda x: x * x, nums))
# print(squared)

# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)

# print("----------------------------")

# temp = [37, 28, 36, 33]

# temper = list(map(lambda x: (x * 9/5) + 32, temp))
# print(temper)

# print("--------------------")

# num = [4, 14, 5, 23, 9]
# numbers = list(filter(lambda x: x > 10, num))
# print(numbers)


# # Inner/ Nested  Function

# def outer(text):
#     def inner():
#         print("inner says: ", text)
#     inner()

# outer("Hello")

# print("------------------------")

# def process_order(item):
#     def inner():
#         print(f"receipt is: {item} price is 2000 ")

#     inner()

# process_order("Book")

# print("-------------------------")

# def process_order(item, price = 2000):
#     def inner(discount):
#         saving = price * (discount / 100) 
#         total = price - saving
    
#         print(f"receipt is: {item} | price is {price} | Discount: {discount}% | Total_bill: {total}")

#     inner(10)

# process_order("Book")

# File Handling

# with open ("note.txt", "w") as f:
#     f.write("Hello Ali Hassan")

# with open ("note.txt", "r") as f:
#     content = f.read()
#     print(content);

# with open("score.txt", "w") as f:
#     f.write("Computer\n ")
#     f.write("Math\n ")
#     f.write("English ")

# with open("score.txt", "r") as f:
#     content = f.read()
#     print(content)

with open("score.txt", "w") as f:
    subj1 = input("Enter Your first Favourite subject:  ")
    subj2 = input("Enter Your second Favourite subject: ")
    subj3 = input("Enter Your third Favourite subject: ")
    f.write(subj1 + "\n")
    f.write(subj2 + "\n")
    f.write(subj3 + "\n")

