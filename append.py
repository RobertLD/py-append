#!/usr/bin/python
import sys
import os
import glob
from os import listdir
from os.path import isfile, join

argLen = len(sys.argv)

if(argLen == 1):
    print("\n" + ("-" * 50))
    print("Usage: python3 append.py Moutput file> <input file(s)>")
    print("To combine all .txt files in current dir, try all")
    print("Example: \"python3 append.py output.txt all\"")
    print(("-" * 50) + "\n" )
    exit()

arguments = sys.argv

#usage


#Parsed Arguments
c = sys.argv[0]
outputFile = sys.argv[1]
inputFiles = arguments[2:]

# ALL command
mypath = os.getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
allTxtFiles = [f for f in glob.glob("*.txt")]

# check for all
if(len(sys.argv) == 3 and sys.argv[2].lower() == 'all' ):
    # ALL has been entered
    filenames = allTxtFiles
    with open(outputFile, 'w') as outfile:
        for fname in filenames:
            outfile.write('\n')
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
else:       
    filenames = inputFiles
    #Combine files
    with open(outputFile, 'w') as outfile:
        for fname in filenames:
            outfile.write('\n')
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)