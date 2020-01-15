"""nester.py
Function print_lol (the_list,num_tab) prints lists of lists with lists indented num_tab times

Grace Davidson
1/14/20
Function to print a list, regardless of how deep the lists are nested
This is accomplished through recursion.

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",[ "Michael Palin","John Cleese","Terry Gilliam", "Eric Idle","Terry Jones"]]] 


"""
#For each item in the given list, if the item is a list, call itself until finished"""

def print_lol(the_list,num_tab): 
	for each_item in the_list:
		if isinstance(each_item,list): 
			for num in range(num_tab):
				print("\t", end='')
			print_lol(each_item, num_tab+1) 
		else: 
			print(each_item)

			
