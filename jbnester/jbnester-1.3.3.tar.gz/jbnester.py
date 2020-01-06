"""This is the jbnester.py module, it provides one function called print_lol()
which prints lists including any nested lists.
Constructed via Head First Python (O'Reilly, Paul Barry)"""

def print_lol(the_list, indent=False, level=0):
    
    """ - 'the_list', any Python list. Each item (recursively) printed to screen on its ownline.
        - 'indent', optional boolean argument to determine if lists should be indented
        - 'level', optional int argument for the number of tab stops to indent by"""

    for item in the_list:
        if isinstance(item, list):
            print_lol(item, indent, level + 1)
        else:
            if indent:
                print("\t" * level, end='')
            print(item)
            
