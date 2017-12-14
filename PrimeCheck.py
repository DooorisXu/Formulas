num = int(input('Enter an integer \n'))
prime = 0
if num > 1:
    for i in range (2,num):
        if (num%i) == 0:
            prime = str('not a prime number')
            print(prime)
            print(str(i)+" * "+str(num//i)+" = "+str(num))
            break
        else:
            prime = num
print(prime,' is a prime number')
