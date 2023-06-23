numbers = input("Input a list of numbers ").split()
numbers = [int(num) for num in numbers] 
max_number = max(numbers)
print("The max number is:", max_number)