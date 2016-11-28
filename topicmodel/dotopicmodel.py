#!/usr/bin/env python

from glob import glob
from os.path import exists
import subprocess
import shlex
import os

# .. means to up a level
source = '../submissions/' #input("Enter name of collection directory: ")
setname = 'submissions' #input("Give this model a name: ")



if not source.endswith('/'):
    source += '/'

if not exists(source):
    print("ERROR: Collection directory does not exist")
    quit()

topics = "10" #input("Enter number of topics to build: ")

# if not topics.isnumeric():
#     print("ERROR: Must enter a valid number")
#     quit()


print("\nPreparing topic model job...\n")

with open(setname + ".lda",mode="w") as file:
    file.write("WORKING=" + source + "\n")
    file.write("TOPICS=" + topics + "\n")
    file.write("SETNAME=" + setname + "\n")
    file.write("ITERATIONS=1000" + "\n")
    
tmcommand = shlex.split("java -jar ichasslda.jar " + setname + ".lda")

subprocess.call(tmcommand)

results = glob(setname + '*')

print("\nTopic model completed. Cleaning up.")
for filename in results:
    if "docvectors.csv" in filename:
        os.rename(filename,setname + "-" + topics + "-documents.csv")
        print("- Document matrix saved as " + setname + "-" + topics + "-documents.csv")
    elif "keys.txt" in filename:
        os.rename(filename,setname + "-" + topics + "-keywords.txt")
        print("- Topic keywords saved as " + setname + "-" + topics + "-keywords.txt")
    elif ".lda" in filename:
        os.remove(filename)