#!/usr/bin/env python
#Python program that runs through the files in 'YeastGenes' folder and finds the GC content of each sequence and total GC content
# transcribes and finds the %AUGC of the third amino acid in the codon

import fileinput
import os
import os.path
from os import path
import glob
import csv
import pandas as pd 

#Reads in seqeunces as elements in list
# header holds the filename in position corresponding to position in sequence
header = list()
sequence = list()
# main program
def main():
    user_seq = "atg"
    #user_seq = input("What sequence do you want to look for?\n")
    user_seq = user_seq.upper()
    tot_file = 0
    path_foldername = "C:\\Users\\sonny\\OneDrive\\Documents\\Bioinformatics Language\\Coding Projects\\R Graph Assignment"
    foldername = 'YeastGenes'
    for filename in os.listdir(foldername):
        #print(filename)
        tot_file += 1
        temp = ""
        my_path = path.join(foldername, filename)
        for line in fileinput.input(files = (my_path)):
            temp += line
        filename = filename[:-4]
        header.append(filename)
        sequence.append(temp)
        #myFile = open("C:\\Users\\gabsbi\\Desktop\\code-examples\\other\\Yeast_RNAseq\\Nagalakshmi_2008_5UTRs_V64.gff3")
        #print(myFile.name)
        #print(myFile.readlines())
    average = 0
    O = open("YeastGeneData.csv", 'w', encoding='UTF8', newline='')
    writer = csv.writer(O)
    csvheader = ["Chromosome","Label", "GC", "SearchedIn", "SearchedInPercent"]
    writer.writerow(csvheader)
    for i in range(len(sequence)):
        average += gcContent(sequence[i], i)
        transcribe(sequence[i])
        times_found = searchForInput(sequence[i], user_seq)
        print("Matches of " + str(user_seq) + " for " + header[i] + " is " + str(searchForInput(sequence[i], user_seq))) # finds and writes the amount of times the string was found
        percentOfInput(sequence[i], times_found, user_seq)
        data = [header[i][1],header[i],gcContent(sequence[i],i),str(user_seq),percentOfInput(sequence[i], times_found, user_seq)]
        writer.writerow(data)
    print("running R script 'Rassignment'\n")
    cmd = './Rassignment.R'
    os.system(cmd)
    print("end script\n")
        
"""def read_csv():
    header = ["Label", "GC", "SearchedIn", "SearchedInPercent"]
    data = [[header[i]],[gcContent(sequence[i],i)],[str(user_seq)],[percentOfInput(sequence[i], times_found,user_seq)]]
    with open("YeastGeneData.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)"""

def searchForInput(seq, user_seq):
    correctCharacters = 0
    times_found = 0
    for i in seq:
        if (correctCharacters == len(user_seq)): # correct, finished, reset
            times_found += 1
            correctCharacters = 0
        elif (i == user_seq[correctCharacters]): # correct
            correctCharacters += 1
        elif (i != user_seq[correctCharacters]): # wrong, reset
            correctCharacters = 0
    return (times_found)

def percentOfInput(seq, times_found, user_seq):
    seq_size = len(seq)
    user_seq_size = len(user_seq)
    seq_percent = float((times_found/(seq_size/user_seq_size))*100)
    seq_percent = round(seq_percent, 3)
    print("Percentage of the entered sequence is: " + str(seq_percent))
    return(seq_percent)

def printS():
    for i in range(len(sequence)):
        print(header[i])
        print(sequence[i] + "\n")
        
        
#Finds GC content 
def gcContent(seq, pos):
    count = 0
    tot = 0
    final = 0
    for i in seq:
        if((i == "C") or (i == "G")):
            count = count + 1
        if((i == "A") or (i == "T")):
            tot = tot + 1
    tot = tot + count
    if(tot !=0):
        final = (count/tot) * 100
    #print("\n\nGC content for ", header[pos], "is ", round(final, 1))
    print(round(final, 1))
    return final

# transcribed sequence to thirdAd()
def transcribe(seq):
    print("\nTranscribing.. \n")
    seq = seq[::-1]
    for i in range(len(seq)):
        if seq[i] == "A":
            seq = seq[:i] + "U" + seq[i+1:]
        elif seq[i] == "T":
            seq = seq[:i] + "A" + seq[i+1:]
        elif seq[i] == "G":
            seq = seq[:i] + "C" + seq[i+1:]
        elif seq[i] == "C":
            seq = seq[:i] + "G" + seq[i+1:]
    thirdAd(seq)

#Finds ratio of AUGC as third amino acid in codon 
def thirdAd(seq):
    Ccount = 0
    Gcount = 0
    Acount = 0
    Ucount = 0
    tot = 0
    for i in range(0, len(seq), 2):
        if seq[i] == "A":
            Acount += 1
            tot += 1
        elif seq[i] == "U":
            Ucount += 1
            tot += 1
        elif seq[i] == "G":
            Gcount += 1
            tot += 1
        elif seq[i] == "C":
            Ccount += 1
            tot += 1
        i += i
    if(tot != 0):
        print("%A at 3rd base ", round(((Acount/tot)*100), 1))
        print("%U at 3rd base ", round(((Ucount/tot)*100), 1))
        print("%G at 3rd base ", round(((Gcount/tot)*100), 1))
        print("%C at 3rd base ", round(((Ccount/tot)*100), 1))
    else:
        print("ERROR: thirdAd is not working correctly") 
    


if __name__ == "__main__":
    main()
    #end script
    print ("\nend myGeneParser.py")
    exit
