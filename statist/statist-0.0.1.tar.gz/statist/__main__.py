from statist import main
import sys

try:
    if len(sys.argv) == 2:
        if len(sys.argv[1]) == 40:
            main()
        else:
            print ('Not a valid token')
    else:
        print ('Not a valid token')
except:
    print ('Not a valid token')
