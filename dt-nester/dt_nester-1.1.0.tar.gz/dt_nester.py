def print_nested_list(the_list, indent=False, level=0):
    for element in the_list:
        if isinstance(element,list):
            print_nested_list(element, indent, level+1)
        else:
            if indent:
                for i in range(level):
                    print("\t", end = '')
            print(element)
