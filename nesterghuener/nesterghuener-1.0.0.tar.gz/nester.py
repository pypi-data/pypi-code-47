"""nester.py
Function print_lol (the_list) prints lists of lists

Grace Davidson
1/14/20
Function to print a list, regardless of how deep the lists are nested
This is accomplished through recursion.
"""
#For each item in the given list, if the item is a list, call itself until finished"""

def print_lol(the_list): 
	for each_item in the_list:
		if isinstance(each_item,list): 
			print_lol(each_item) 
		else: 
			print(each_item)

			
