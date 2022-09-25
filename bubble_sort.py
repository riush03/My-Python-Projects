import random

def sortArray(my_array):
    n: int = len(my_array)
    for i in range(n):
        for j in range(0,n-i-1):
            if my_array[j] > my_array[j+1]:
                temp: int = my_array[j]
                my_array[j]  = my_array[j+1]
                my_array[j+1] = temp

if __name__ == "__main__":
    array: list = []
    for i in range(0,10):
        some_nums: int = random.randint(0,200)
        array.append(some_nums)

    print("Original array")
    for i in array:
        print(i,end=" ")

    print("\n The sorted array")
    sortArray(array)
    for i in array:
        print(i,end=" ")