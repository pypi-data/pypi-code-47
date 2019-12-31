def print_lol(prtlist,level=0):
    for item in prtlist:
        if isinstance(item,list):
            print_lol(item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end="")
            print(item)

movies=['The Holy Grail',1975,'Terry Jones & Terry Gilliam',91,
        "Main:",['Graham Chapman',
                 "Mini:",
         ["Michael Palin",'John Cleese','Terry Gilliam','Eric Idle','Terry Jones']]]
print_lol(movies)