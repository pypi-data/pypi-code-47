"""
nester.py
Function print_lol (the_list,indent=false,num_tab=0) prints lists of lists with lists indented num_tab times

Grace Davidson
1/14/20
Function to print a list, regardless of how deep the lists are nested
This is accomplished through recursion.

	
For each item in the given list, if the item is a list, call itself until finished"""

def print_lol(the_list,indent=False,num_tab=0): 
	for each_item in the_list:
		if isinstance(each_item,list): 
			print_lol(each_item, indent, num_tab+1) 
		else: 
			if indent:
				for num in range(num_tab):
					print("\t", end='')			
			print(each_item)

			
