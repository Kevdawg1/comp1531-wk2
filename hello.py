#!/bin/python3.5
import sys
n = int (sys.argv[1])
strOut = ""
if (n % 3 == 0):
	strOut = strOut + "Fizz "
if (n % 5 == 0):
	strOut = strOut + "Buzz"
if (strOut == ""):
	print (n)
else:	
	print (strOut)
