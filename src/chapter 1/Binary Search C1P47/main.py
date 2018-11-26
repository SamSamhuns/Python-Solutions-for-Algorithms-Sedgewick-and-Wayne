# Chapter 1 Page 47
# Binary Search Whitelist filtering
'''
Filters and prints out unique sequences of numbers in tinyT.txt compared to tinyW.txt
Use case from Algorithms book
Specifically, imagine a credit card company that needs to check
whether customer transactions are for a valid account. To do so, it can
■ Keep customers account numbers in a file, which we refer to as a whitelist.
■ Produce the account number associated with each transaction in the standard
input stream.
■ Use the test client to put onto standard output the numbers that are not associat-
ed with any customer. Presumably the company would refuse such transactions.
'''
import random
import time


# Generating the whitelist files and test files by random
fpw_gen = open( 'tinyW.txt', 'w')
fpt_gen = open( 'tinyT.txt', 'w')

# Number of random numbers to generate
num = 1000
for n in range( 1, num ):
  fpw_gen.write( str(random.randint(100, 500 ))+ ' ')
  fpt_gen.write( str(random.randint(100, 500 ))+ ' ')

fpw_gen.close()
fpt_gen.close()

# Name of files for input and whitelisting
fpw = open( 'tinyW.txt', 'r')
fpt = open( 'tinyT.txt', 'r')

# Binary search main function
def rank ( key, arr ):
  # Input arr must be sorted to use binary search
  minN = 0
  maxN = len(arr) - 1
  while ( min <= max):

    mid = minN + ( maxN - minN ) // 2
    if key < int(arr[mid]):
      maxN = mid - 1
    elif key > int(arr[mid]):
      minN = mid + 1
    else:
      return mid
  return -1

# Fucntion to print non mathcing elements
def b_search():
  whitelist = fpw.read().strip().split()
  testlist = fpt.read().strip().split()

  for key, val in enumerate(whitelist):
    whitelist[key] = int(whitelist[key]
    
  whitelist.sort()

  for elem in testlist:
    if rank( int(elem), whitelist ) < 0:
      print( elem ) 
      
# Time execution of binary search filter print
start_time = time.time()
b_search()
print("--- %s seconds ---" % (time.time() - start_time))

fpw.close()
fpt.close()
