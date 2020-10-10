import random

# list out all the attributes in the random module
# print(dir(random))

# Generate random number with in the default range - 0.0 to 1.0
print(random.random())      # float[0.0 to 1.0]

print(random.uniform(10, 20)) # float [10 to 20]

print(random.randint(10, 20))

# Odd
print(random.randrange(1, 10, 2)) # start = 1, end = 10 -1, step = 2 [1 3 5 7 9]

# even
print(random.randrange(2, 10, 2)) # start = 1, end = 10 -1, step = 2 [2 4 6 8 10]

# choice
lst = ['dev', 'test', 'devops', 'ds']
print(random.choice(lst))


# choices
print(random.choices(lst, k=6))


desk = list(range(1, 53))
print(desk)

random.shuffle(desk)
print(desk)

print(random.sample(desk, k = 10))

