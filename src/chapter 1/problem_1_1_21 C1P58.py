# Chapter 1 Page 58
# Problem 1.1.21
'''
Write a program that reads in lines from standard input with each line containing a name and two integers and then uses printf() to print a table with a column of the names, the integers, and the result of dividing the first by the second, accurate to three decimal places. You could use a program like this to tabulate batting averages for
baseball players or grades for students.
'''
# Assumed input file is in CSV format
# Run the file with command python3 problem_1_1_21\ C1P58.py info.csv
import sys
import random as rd

# Code to generate name, int A, int B csv format file with random names
fw = open( "info.csv", 'w' )
print( "name, A, B", file=fw)

for i in range(100):
  print( "".join( [ chr(round(rd.randint(97 , 123), 0)) for x in range( round(rd.randint(5,16), 0) )]), file=fw, end=', ')
  print( round(rd.randint(5,16), 0), ", ", round(rd.randint(5,16), 0), file=fw, end='\n' )
fw.close()


# Code to print out the data
tb = []
temp = []
fp = open( sys.argv[1], 'r')
temp.extend((fp.readline()).strip().split(','))
temp.extend(["A/B"])
tb.append( temp )

for line in fp:
  line = line.strip().split(',')
  line.extend( [round(int(line[1])/int(line[2]), 3)] )
  tb.append( line )

for elem in tb:
	print( elem )

fp.close()
