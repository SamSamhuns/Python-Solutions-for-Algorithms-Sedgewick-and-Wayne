# Chapter 1 Page 58
# Problem 1.1.22
'''
Write a version of BinarySearch that uses the recursive rank() given on page 25 and traces the method calls. Each time the recursive method is called, print the argument values lo and hi, indented by the depth of the recursion. Hint: Add an argument to the recursive method that keeps track of the depth.
ATTENTION: TENTATIVE SOLUTION
'''

import random as rd

# Binary Search Algorithm using recursion
def rank ( key, arr, imin ,imax, depth ):
  # arr must be a sorted array
  depth += 1
  print( "\t"*depth ,"lo = ", imin, "   hi = ", imax)
  if ( imin > imax ):
    return -1
  mid = imin + ((imax - imin) // 2)
  if ( key < arr[mid] ):
    return rank( key, arr, imin, mid-1, depth )
  elif ( key > arr[mid] ):
    return rank( key, arr, mid+1, imax, depth )
  else:
    return mid

# Genrating a unqiue list of 50 random numbers from 1 to 100
r_arr = rd.sample(range(1, 100), 50)
r_arr.sort()
print ( rank( 56, r_arr, 0, len(r_arr)-1, 1) )
