#!/usr/bin/env python2
import sys
name = sys.stdin.read()

def Multiply(num1, num2):
	answer = num1 * num2
	return answer

def Divide(num1, num2):
	answer = num1 % num2
	return answer

def Add(num1, num2):
	answer = num1 + num2
	return answer

def Subtract(num1, num2):
	answer = num1 - num2
	return answer

print "I'm going use the calculator functions to multiply 5 and 6"
x = Multiply(5,6)
print x