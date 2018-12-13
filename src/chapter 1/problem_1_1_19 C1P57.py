# Chapter 1 Page 57
# Problem 1.1.19
'''
Fibonacci Generator improvement
'''

#Old function using recursion
'''
def F(N):
	if N == 0:
		return 0
	if N == 1:
		return 1
	return F(N-1) + F(N-2)
'''

f_arr = [0]

# New function making use of an array
def F(N):
  if N == 0:
    f_arr.extend( [N] )
    N = 1
  elif N == 1:
    f_arr.extend( [N] )
    return ( f_arr[N-1] + f_arr[N-2] )
  else:
    f_arr.extend( [f_arr[N] + f_arr[N-1]] )
  return ( f_arr[N] + f_arr[N-1] )

def main():
  for i in range(0, 100):
    print( i, " ", F(i))

main()
