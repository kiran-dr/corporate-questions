# 1. Python program to give sum of all cubes from m to n
m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
sum=0
if m>n :
  print("Enter valid m,n values")
else:
  for x in range(m,n+1):
    sum=sum+x**3
  print(f"sum of cubes from {m} to {n} = {sum}")

# 2. Python program to give product of numbers from m to n
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
if m > n:
    print("Enter valid m,n values")
else:
    output = 1
    for x in range(m, n + 1):
        output = output * x
    print(f"Product of integers from {m} to {n} = {output}")


# 3. Python program to give product of all even numbers from m to n
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
if m > n:
    print("Enter valid m,n values")
else:
    output = 1
    for x in range(m, n + 1):
        if x % 2 == 0:
            output = output * x
    print(f"Product of even numbers from {m} to {n} = {output}")


# 4. Python program to give product of all odd numbers from m to n
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
if m > n:
    print("Enter valid m,n values")
else:
    output = 1
    for x in range(m, n + 1):
        if x % 2 != 0:
            output = output * x
    print(f"Product of odd numbers from {m} to {n} = {output}")


# 5. Python program to give sum of all factorial numbers from m to n
m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
if m>n :
  print("Enter valid m,n values")
else:
  sum=0
  fact1 = 1
  for i in range(m,n+1):
    for j in range (1,i+1):
      fact1 = fact1*j
    sum=sum+fact1
    fact1=1
  print(f"sum of factorial numbers from {m} to {n} = {sum}")


# 6. Python program to give sum of all prime numbers from m to n
m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
if m>n :
  print("Enter valid m,n values")
else:
  sum=0
  for i in range (m,n+1):
    if i<=1:
      continue
    else:
      is_prime=True
      for j in range(2,int(i**0.5)+1):
          if i%j==0:
            is_prime=False
            break
      if is_prime==True:
        sum=sum+i
  print(f"sum of prime numbers from {m} to {n} = {sum}")
