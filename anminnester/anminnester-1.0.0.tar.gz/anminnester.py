'''-------------------------'''
def print_lol(the_list):
    '''________________________'''
    for i in the_list:
        if isinstance(i,list):
            print_lol(i)
        else:
             print(i)