# Ternary

# age = 17
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# marks = 39
# result = "Pass" if marks >= 40 else "Fail"
# print(result)

# Break, Continue, Pass

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(6):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(20):
#     if i == 15:
#         break
#     print(i + 1)

# for i in range(21):
#     if i % 3 == 0:
#         continue
#     print(i)


# For Loop
# foods = ["rice", "pizza", "burger", "briyani", "fries"]
# for index,food in enumerate(foods):
#     print(index, food)

# print("--------------")

# for i in range(10):
#     print(i ** 2)


# While Loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# num = 2
# while num <= 20:
#     print(num)
#     num += 2

# num = 10
# while num > 0:
#     print(num)
#     num -= 1

# print("Liftoff!")

# Nested Loop

# for i in range(1,4):
#     for j in range(1, 4):
#         print(i, "x", j, "=", i*j)


for i in range(1, 6):
    for j in range(1, 6):
        print(i, "x" ,j, "=", i*j)

print("--------------")

for i in range(1,6):
    for  j in range(1):
        print("*" * i)

print("----------------")

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("------------------")

for i in range(2, 3):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)