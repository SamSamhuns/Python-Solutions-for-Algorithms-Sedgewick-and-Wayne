# Chapter 1 Page 56
# Problem 1.1.13
'''
Write a code fragment to print the transposition (rows and columns changed)
of a two-dimensional array with M rows and N columns.
'''
arr = [[1, 2, 3, 4], [5, 6, 7, 8]] 

# creating an empty transposed matrix to receive elements from the old matrix
trans_mat = []
for row in range(0, len(arr[0])):
  add_list = []
  for col in range(0, len(arr)):
    add_list.extend([" "])
  trans_mat.append(add_list)   

# Transpose function
def transpose ( arr ):
  for row in range(0, len(arr)):
    for col in range(0, len(arr[0])):
      trans_mat[col][row] = arr[row][col]

transpose ( arr )
print ( trans_mat )