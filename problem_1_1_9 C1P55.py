# Chapter 1 Page 55
# Problem 1.1.9
'''
Write a code fragment that puts the binary representation of a positive integer N
into a String s.
'''
s = ""

def int_to_bin ( N ):
  result = ""
  while N != 0:
    rem = N % 2
    N = N / 2
    result = str(rem) + result
  s = result
  print(s)

int_to_bin( 15 )