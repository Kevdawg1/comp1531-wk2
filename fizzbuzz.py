#!/bin/python3.5
import sys
def FizzBuzz(n):
	strOut = ""
	if (n % 3 == 0):
		strOut = strOut + "Fizz "
	if (n % 5 == 0):
		strOut = strOut + "Buzz"
	if (strOut == ""):
		print (n)
	else:	
		print (strOut)

if(len(sys.argv) == 2):
	n = int (sys.argv[1])
	FizzBuzz(n)
