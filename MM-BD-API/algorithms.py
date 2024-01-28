import math
from typing import Iterator

def linear_congruential_generator(m, a, c, seed) -> Iterator[int]:
    x = seed
    while True:
        x = (a * x + c) % m
        yield x

def shuffle_by_algorithm_M(X:list, Y:list, k, n):
    if len(X) < k:
        raise ValueError("X must have at least k elements")
    mod_Y = max(Y)+1
    V = []
    V = X[0:k]
    x_index = k 
    y_index = 0 
    shuffled_X = []
    while n > 0:
        if x_index == len(X):
            x_index = 0
        if y_index == len(V):
            y_index = 0
        x = X[x_index]
        y = Y[y_index]
        j = math.floor((k*y)/mod_Y)
        shuffled_X.append(V[j])
        V[j] = x
        x_index += 1
        y_index += 1
        n -= 1
    return shuffled_X

def shuffle_by_algorithm_M_with_Iterator(X:Iterator[int], Y:Iterator[int], k, mod_Y, n):

    V = []
    V = [next(X) for _ in range(k)]
    
    shuffled_X = []

    while n > 0:
        x = next(X)
        y = next(Y)
        j = math.floor((k*y)/mod_Y)
        shuffled_X.append(V[j])
        V[j] = x
        n -= 1
    
    return shuffled_X

def shuffle_by_algorithm_B(X:list, k, n):
    if len(X) < k+1:
        raise ValueError("X must have at least k elements")

    V = []
    V = X[0:k]
    x_index = k 
    if x_index == len(X):
        x_index = 0
    Y = X[x_index]
    x_index += 1
    shuffled_X = []
    mod = max(X)+1
    
    while n > 0:
        if x_index == len(X):
            x_index = 0
        j = math.floor((k*Y)/mod)
        Y = V[j]
        shuffled_X.append(Y)

        V[j] = X[x_index]

        x_index += 1
        n -= 1
    
    return shuffled_X

def shuffle_by_algorithm_B_with_Iterator(X:Iterator[int], k, mod, n):

    V = []
    V = [next(X) for _ in range(k)]
    Y = next(X)
    shuffled_X = []
    
    while n > 0:

        j = math.floor((k*Y)/mod)
        Y = V[j]
        shuffled_X.append(Y)
        V[j] = next(X)
        n -= 1
    
    return shuffled_X

#TODO use modulus rather than len(X)

    