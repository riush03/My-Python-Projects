#declare an array and intialize it
array: list = [100,200,500,230,140,
               400,600,150,135,534,
               390,430,160,260,710]

search: int = int(input("Enter the number you want to search:"))
position: int = 0
target: int = 0
for i in array:
    target = target+1
    if i == search:
        position = target

if __name__ == "__main__":
    if target == 15 and position == 0:
        print(f"`{search} ` cannot be found in this array.")
    else:
        print(f" `{search}` is loacted at position `{position}` in the array.")
