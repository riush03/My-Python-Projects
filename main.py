#read files with python
import random

my_shopping_list = (random.randint(0,500) for i in range(10))

#writing to a file
with open("data.txt","w") as file:
    for idx,num in enumerate(my_shopping_list):
        file.write(f"`{idx}`:`{num}` \n")

#reading a file
with open("data.txt","r") as file:
    lines = file.readlines()
    items = list()
    for line in lines:
        item = line.split(':')
        num = item[1].split(' ')
        items.append(num[0])

if __name__ == "__main__":
    sum: int = 0
    even_nums: int = 0
    odd_nums: int = 0
    for i in items:
        if int(i) % 2 == 0:
            even_nums += 1
        else:
            odd_nums += 1
        sum += int(i)

    print(f"Even numbers: `{even_nums} piece\n"
          f"Odd numbers: `{odd_nums} piece\n"
          f"Sum: `{sum}`")