# Chapter 1 Page 54
# Problem 1.1.3
'''
Write a program that takes three integer command-line arguments and prints
equal if all three are equal, and not equal otherwise.
'''
import sys 
# IMPORTANT
# run the program as python problem_1_1_3.py arg1 arg2 arg3
# the three arguments must be integers

def triple_check ( a1, a2, a3 ):
  if (a1 == a2) and (a1 == a3):
    result = ""
  else:
    result = " not "
  print ( a1, " ", a2, " ", a3, " ", "are", result, "equal" )


triple_check( int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) )
