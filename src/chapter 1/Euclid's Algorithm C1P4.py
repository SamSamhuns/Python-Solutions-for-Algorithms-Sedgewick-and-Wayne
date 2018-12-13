# Chapter 1 Page 4
# Euclid's Algorithm

'''
Compute the greatest common divisor of
two nonnegative integers p and q as follows:
If q is 0, the answer is p. If not, divide p by q
and take the remainder r. The answer is the
greatest common divisor of q and r.
'''

def gcd( p, q ):
  if q == 0 :            # Base case
    return p
  r = p % q
  return gcd(q, r)       # Recursive approach
