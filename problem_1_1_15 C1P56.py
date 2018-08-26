# Chapter 1 Page 56
# Problem 1.1.15
'''
Write a static method histogram() that takes an array a[] of int values and
an integer M as arguments and returns an array of length M whose ith entry is the number of times the integer i appeared in the argument array. If the values in a[] are all between 0 and M–1, the sum of the values in the returned array should be equal to a.length.
'''
import random as rd

def histogram( int_arr, M):
  res_arr = []
  for i in range(0, M-1):
    res_arr.extend( [int_arr.count(i)] )
  return res_arr

# Generating a randomly filled integer
arr = [ round(rd.randint(1,13),0) for i in range(100) ]

print ( histogram( arr , 15 ) )

# Proof for the second case in the question
print ( len(arr), sum(histogram( arr , 15 ) ) )