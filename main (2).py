n = int(input("Input number "))
num1 = 0
num2 = 1
next_number = 0
sum = 1
  
while(sum <= n):
    print(next_number, end=" ")
    sum += 1
    num1 = num2
    num2 = next_number
    next_number = num1 + num2
