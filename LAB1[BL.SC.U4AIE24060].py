
def count(Str):
  vowels = 0
  consonants = 0
  for i in Str:
    if i in ['a', 'e', 'i', 'o', 'u']:
      vowels += 1
    else:
      consonants += 1

  return (vowels, consonants)

print(count("hello world"))

import numpy
def matrixMultiplication(A, B):
  try:
    return numpy.array(A)*numpy.array(B)
  except Exception as e:
    return "Matrix not compatible"

A = [[1,1], [2,2], [3,3]]
B = [[0,0,0], [0,0,0], [0,0,0]]

print(matrixMultiplication(A, B))

A = [[1,1,1], [2,2,2], [3,3,3]]
B = [[0,0,1], [0,0,1], [2,2,1]]

print(matrixMultiplication(A, B))

def common(lst1, lst2):
  set1 = set(lst1)
  set2 = set(lst2)

  return set1.intersection(set2)

print(common([1,2,3], [2,3,4]))

def transpose(matrix):
  for i in range(len(matrix)):
    for j in range(i):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  return matrix

print(transpose([[1,2,3], [4,5,6], [7,8,9]]))

import random

def calculate(numbers):
    total = 0
    for value in numbers:
        total += value
    mean = total / len(numbers)

    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)

    if n % 2 == 0:
        median = (numbers_sorted[n // 2 - 1] + numbers_sorted[n // 2]) / 2
    else:
        median = numbers_sorted[n // 2]

    frequency = {}
    for value in numbers:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_count = 0
    mode = None
    for key in frequency:
        if frequency[key] > max_count:
            max_count = frequency[key]
            mode = key

    return mean, median, mode


numbers = [random.randint(100, 150) for _ in range(100)]
mean, median, mode = calculate(numbers)
print("Numbers:", numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
