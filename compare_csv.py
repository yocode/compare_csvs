# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:02:34 2016

@author: jsklein
"""
import pandas as pd
import csv
import argparse

# Parse command line arguments and set them to variables to be used later
def main():
    parser = argparse.ArgumentParser(description='Compares two CSV files for matches and differences indexed on a column')

    parser.add_argument("-i", help="Name of first CSV import file", action="store", dest="infile1", required="yes")
    parser.add_argument("-I", help="Name of second CSV import file", action="store", dest="infile2", required="yes")
    parser.add_argument("-c", help="Name of column to index on", action="store", dest="column", required="yes")
    
    args = parser.parse_args()    
    file1 = args.infile1
    file2 = args.infile2
    column = args.column
    print(file1)
    print(file2)

    # explicitly call the other functions
    merge_csvs(file1,file2,column)
    diff_csvs(file1,file2)

# Define Compare funtion that joins on specified column
def merge_csvs(file1,file2,column):
    a = pd.read_csv(file1)
    b = pd.read_csv(file2)
    print(a)
    print(b)

    merged = b.merge(a, on=column)
    merged.to_csv("merged_results.csv", index=False) 

# Define Diff function that diffs on specified column
def diff_csvs(file1,file2):
    s = open(file1, 'r')
    k = open(file2, 'r')
    print(s)
    print(k)

    checkS = csv.reader(s)
    checkK = csv.reader(k)

    output1 =  [row for row in checkS if row not in checkK]
    output2 =  [row for row in checkK if row not in checkS]

    with open("A_notin_B.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(output1)

    with open("B_notin_A.csv", "w") as l:
        writer = csv.writer(l)
        writer.writerows(output2)

# Main Function that Calls all the other functions
main()