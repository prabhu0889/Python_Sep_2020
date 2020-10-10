# file = open('text1.txt', mode='w')
# file.write("hello everyone")
# file.close()

# Way 1
file = open('text2.txt', mode='w')
for i in range(1, 11):
    file.write(f'Hi all, gud noon {i} \n')
print(file.closed)
file.close()
print(file.closed)

# Way 2
with open('text3.txt', mode='w') as file:
    for i in range(10):
        file.write(f'5 * {i} = {5 * i}\n')