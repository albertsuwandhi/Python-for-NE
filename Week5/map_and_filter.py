#!/usr/bin/env python3
#LAMBDA

#normal function
def pangkat(x):
    return x**2
print(pangkat(9))

#lambda function
lambda_pangkat = lambda x: x**2
print(lambda_pangkat(5))

#map
output = map(lambda x : x*2, [2,4,6,8])
print(list(output))
#filter
output = filter(lambda x : x%2==0,range(10))
print(list(output))

