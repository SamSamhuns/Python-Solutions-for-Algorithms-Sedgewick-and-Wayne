# Chapter 1 Page 58
# Problem 1.1.23
# Binary Search Whitelist filtering
'''
Filters and prints out unique sequences of numbers in tinyT.txt compared to tinyW.txt
Use case from Algorithms book

Add to the BinarySearch test client the ability to respond to a second argu-
ment: + to print numbers from standard input that are not in the whitelist, - to print

numbers that are in the whitelist.
'''
import random as rd
import time
import sys

# When executing the program, a "+" or "-" cmd line argument must be used
# i.e. python3 problem_1_1_22\ C1P58.py +
# Generating the whitelist files and test files by random
fpw_gen = open( 'tinyW.txt', 'w')
fpt_gen = open( 'tinyT.txt', 'w')

# Number of random numbers to generate
num = 1000
for n in range( 1, num ):
  fpw_gen.write( str(rd.randint(100, 500 ))+ ' ')
  fpt_gen.write( str(rd.randint(100, 500 ))+ ' ')

fpw_gen.close()
fpt_gen.close()

# Name of files for input and whitelisting
fpw = open( 'tinyW.txt', 'r')
fpt = open( 'tinyT.txt', 'r')

# Binary search main function
def rank ( key, arr ):
  # Input arr must be sorted to use binary search
  min = 0
  max = len(arr) - 1 
  while ( min <= max):

    mid = min + ( max - min ) // 2
    if key < int(arr[mid]):
      max = mid - 1
    elif key > int(arr[mid]):
      min = mid + 1
    else:
      return mid
  return -1

# Function to print non mathcing elements
def b_search( result_type ):
  whitelist = fpw.read().strip().split()
  testlist = fpt.read().strip().split()

  for eInd in range(0, len(whitelist)):
    whitelist[eInd] = int( whitelist[eInd] )
  
  whitelist.sort()

  for elem in testlist:
    if result_type == "+" and (rank( int(elem), whitelist ) < 0):
      print( elem ) 
    elif result_type == "-":
      print( elem )
      
# Time execution of binary search filter print
start_time = time.time()
b_search( sys.argv[1] )
print("--- %s seconds ---" % (time.time() - start_time))

fpw.close()
fpt.close()
