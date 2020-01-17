import sys

def testlire(filename):
    with open(filename, 'rb') as ff:  #, encoding='UTF-8'
        line = ff.readline()
        while line:
            #val = line.decode("ISO-8859-15") 
            val = line.decode("UTF-8") 
            print(val.rstrip(), file=sys.stderr) 
            line = ff.readline()
            # val = ff.read().decode("ISO-8859-15") 

if __name__ == "__main__":
    filename = "/Users/jeanluc/docker_work/python3-based/nn1/publi_2/help.txt"
    testlire(filename)