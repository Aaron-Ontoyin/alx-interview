#!/usr/bin/env python3
"""
This module contains a function that finds min operations to get n H's in a file.
Check readme for more details
"""


def minOperations(n):
	if n <= 1:
		return 0

	#copyAll and Paste for first time
	num_operations = 2
	num_H = 2
	clipboard_H = 1

	# possible = True
	while num_H != n:
		if n % num_H == 0:
			num_operations += 2
			clipboard_H = num_H
			num_H += num_H
		else:
			num_operations += 1
			num_H += clipboard_H
		# if num_H > n:
		# 	possible = False
		# 	break

	return num_operations

minOperations(5)