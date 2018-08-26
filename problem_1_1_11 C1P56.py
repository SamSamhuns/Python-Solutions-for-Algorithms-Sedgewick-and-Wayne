# Chapter 1 Page 56
# Problem 1.1.11
'''
Write a code fragment that prints the contents of a two-dimensional boolean
array, using * to represent true and a space to represent false. Include row and column
numbers.
'''

def bool_arr_print ( arr ):
  for i in arr:
    for j in i:
      if j == True: 
        print('*', end=" ")
      else:
        print('_', end=" ")
    print('\n')

bool_arr_print( [[True, False, False, True], [ False, True ]] )