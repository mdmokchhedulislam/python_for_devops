# reverse
a= "hellow world"

def reve_str(s):
    return s[::-1]


# print(reve_str(a))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# print(is_prime(36))

# n= int(input("enter your number for check total: "))
n=10
sum = 0 
for i in range(1, n+1):
    sum +=i

# print(sum)


# comprehension of list 


square = []

n = int(input("enter your number for create list"))

for i in range(n+1):
    square.append(i*i)

print(square)

