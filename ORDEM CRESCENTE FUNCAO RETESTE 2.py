def n(n1,n2,n3):
  if n1 > n2: 
    if n1 > n3:
      if n2 > n3:
        return f'{n3}\n{n2}\n{n1}'
      else:
        return f'{n2}\n{n3}\n{n1}'

  elif n2 > n3:
    if n2 > n1:
      if n1 > n3:
        return f'{n3}\n{n1}\n{n2}'
      else:
        return f'{n1}\n{n3}\n{n2}'

  elif n3 > n2:
    if n3 > n1:
      if n1 > n2:
        return f'{n2}\n{n1}\n{n3}'
      else:
        return f'{n1}\n{n2}\n{n3}'
    
     
num1 = int(input())
num2 = int(input())
num3 = int(input())

ch1 = n(num1, num2, num3)

print(ch1)