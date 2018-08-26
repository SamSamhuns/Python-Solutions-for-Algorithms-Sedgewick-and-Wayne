# Chapter 1 Page 56
# Problem 1.1.14
'''
Write a static method lg() that takes an int value N as argument and returns
the largest int not larger than the base-2 logarithm of N. Do not use Math.
'''

def lg(N):
  div = 0
  while True:
    if (2 ** div) == N:
      break
    if (2 ** div) > N:
      div -= 1
      break
    div += 1
  return div

print ( lg(64) )