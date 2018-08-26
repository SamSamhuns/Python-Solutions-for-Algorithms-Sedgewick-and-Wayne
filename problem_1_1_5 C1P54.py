# Chapter 1 Page 54
# Problem 1.1.5
'''
Write a code fragment that prints true if the double variables x and y are both
strictly between 0 and 1 and false otherwise.
'''

def double_lim_check ( x, y ):
  x = float(x)
  y = float(y)
  if (x < 1.0 and x > 0.0) and (y < 1.0 and y > 0.0):
    return True
  else:
    return False

print ( double_lim_check( 0.442, 0.999999 ))