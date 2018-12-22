choice = int(input("How many numbers do you wanna see? "))
fibonacci = [0,1]

for i in range(1,choice):
    fibonacci.append(fibonacci[i]+fibonacci[i-1])
    print(fibonacci[1:choice+1])

