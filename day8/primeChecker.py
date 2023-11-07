def prime(num):
  is_prime = True
  for i in range(2,num-1):
    if num%i == 0:
      is_prime = False

  if is_prime == True:
    print("Its a prime number")
  else:
    print("Its not a prime number")


prime(7)
prime(17)
prime(27)
prime(53)
prime(91)
prime(31)
    
