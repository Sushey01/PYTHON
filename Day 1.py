def print_star_pattern(num):
    for i in range(1, num+1):
        print(i)
        print('*' * i)
n=int(input("Please enter a number:"))
print_star_pattern(n)