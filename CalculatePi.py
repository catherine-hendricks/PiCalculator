import math
from decimal import Decimal, getcontext

getcontext().prec = 100

#create list to hold terms of summand
summand = []

#calculate terms of summand
iteration = 5
for n in range(iteration):

    num1 = Decimal(math.factorial(4*n))/Decimal((math.factorial(n)**4))
    num2 = Decimal((1103 + 26390 * n))/Decimal((396 ** (4 * n)))

    num3 = num1 * num2

    summand.append(num3)

#add them together for sum
sum = 0
for i in range(len(summand)):
    sum += summand[i-1]

#multiply by coefficient
coefficient = Decimal(2) * Decimal(math.sqrt(2)) / Decimal(9801)
inverse = coefficient * sum

#take the inverse
pi = 1/inverse

print(pi)
print(type(sum))
print(summand)

#print out just the exponent for each term

#print each digit of summand[i] one by one until you get to that exponent

#then add the next number etc.