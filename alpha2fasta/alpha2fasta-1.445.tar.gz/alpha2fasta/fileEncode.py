from re import sub,findall,search
import unidecode
from Bio import SeqIO
import sys
from AMINOcode import *
from DNAbits import *
import codecs

def fileEncode(input_file,output_file,method_name='aminocode',reverse=False,header_format='number'):
    if method_name == 'aminocode':
        selectedEncoder = AMINOcode
        if reverse:
            selectedEncoder = AMINOcode_reverse
    elif method_name == 'dnabits':
        selectedEncoder = DNAbits
        if reverse:
            selectedEncoder = DNAbits_reverse
    elif method_name == 'aminocode_simplified':
        selectedEncoder = lambda x: AMINOcode(x,simplified=True)
        if reverse:
            selectedEncoder = lambda x: AMINOcode_reverse(x,simplified=True)
    if reverse:
        print('Decoding text...')
        outputFile = codecs.open(output_file,'w')
        records = list(SeqIO.parse(input_file, "fasta"))
        num_lines = len(records)
        c=0
        for i in records:
            c+=1
            if Entry1 != 0:
                if (c+1) % 1000 == 0:
                    Entry1.set(c+1)
                    myWin.update()
            else:
                if (c+1) % 10000 == 0:
                    print(str(c+1)+'/'+str(num_lines))
            outputFile.write((selectedEncoder(str(i.seq))+'\n'))
        outputFile.close()
        print(str(num_lines)+'/'+str(num_lines))
        return
            
            
    inputFile = open(input_file,'r')
    try:
        records = list(SeqIO.parse(input_file, "fasta"))
        t = type(records[0])
        inputFile.close()
        inputFile = []
        for i in records:
            inputFile.append (i.description)
    except:
        pass
        
    count = 0
    header = []
    for i in inputFile:
        count += 1
        if header_format == 'number':
            header.append(count)
        elif header_format == 'originaltext':
            i = sub('\n$','',i)
            header.append(i)
    try:
        inputFile.close()
        inputFile = open(input_file,'r')
    except:
        pass
        
    outputList = []

    print ('Encoding text...')
    print ('0'+'/'+str(count))
             
    for c,i in enumerate(inputFile):
        i = sub('\n$','',i)
        outputList.append('>'+str(header[c])+'\n')
        try:
            i = i.decode('utf-8')
        except:
            pass
        seq = selectedEncoder(i)
        seq = findall('\w{0,'+str(100)+'}',seq)
        seq = '\n'.join(seq)
        outputList.append(seq)
        if (c+1) % 10000 == 0:
            print (str(c+1)+'/'+str(count))
    print (str(count)+'/'+str(count))
    try:
        inputFile.close()
    except:
        pass
    outputFile = open(output_file,'w')
    for i in range(1,len(outputList),2):
        if search('\w+',outputList[i]):
            outputFile.write (outputList[i-1])
            outputFile.write (outputList[i])
    outputFile.close()
    print ('Finish!')
fe=fileEncode