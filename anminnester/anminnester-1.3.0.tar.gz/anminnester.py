# '''-------------------------'''
# def print_lol(the_list):
#     '''________________________'''
#     for i in the_list:
#         if isinstance(i,list):
#             print_lol(i)
#         else:
#             print(i)

# '''-------------------------'''
# def print_lol(the_list,level):
#     '''________________________'''
#     for i in the_list:
#         if isinstance(i,list):
#             print_lol(i,level+1)
#         else:
#             for tab_stop in range(level):
#                 print('\t',end='')
#             print(i)

# '''-------------------------'''
# def print_lol(the_list,level=0):
#     '''________________________'''
#     for i in the_list:
#         if isinstance(i,list):
#             print_lol(i,level+1)
#         else:
#             for tab_stop in range(level):
#                 print('\t',end='')
#             print(i)

'''-------------------------'''
def print_lol(the_list,indent=False,level=0):
    '''________________________'''
    for i in the_list:
        if isinstance(i,list):
            print_lol(i,indent,level+1)
        else:
            if indent==True:
                for tab_stop in range(level):
                     print('\t',end='')
            print(i)
