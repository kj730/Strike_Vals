#!/usr/bin/python
import sys
import numpy as np
DATE_COL = 9
SV_COL = 11
STRIKE_COL = 0
VALUE_COL = 1
LINE_COL = 7
#finds the strike value of a given file
def Strike_Value(filename, year, month):
    strikeArr = []
    tempArr = []
    combineArr = []
    try:
        filer = open(filename, "r")
    except OSError as err:
        print("Unable to open File. OS error: {0}".format(err))
        return -1
    except:
        print("Unable to open File")
        return -1
    for line in filer:
        pound_pos = line.find('#')
        newLine = line[:pound_pos]
        splitter = newLine.split('|')
        if splitter[LINE_COL] == "1":
            continue
        #adds strikes to an array if they are in the correct month
        if splitter[DATE_COL] == month + "/" + year:
            if len(combineArr) == 0:
                combineArr = splitter[SV_COL].split(':')
            #combines teh array if there is already one with data in it    
            else:
                tempArr = splitter[SV_COL].split(':')
                combineArr += tempArr
    filer.close()
    return combineArr
#formats the output to be easier to read
def format_output(data):
    count = 1
    checker = ""
    for x in data:
        arr = x.split('/')
        value = arr[VALUE_COL]
        print("Strike = " + arr[STRIKE_COL] + "\tValue = " + value)
        count = count + 1
        
def main():
    if len(sys.argv) < 3:
        print("Usage: ", sys.argv[0], "Filename Year Month")
        exit(-1)
    filename = sys.argv[1]
    year = sys.argv[2]
    month = sys.argv[3]
    answerArr = Strike_Value(filename, year, month)
    format_output(answerArr)
if __name__ == "__main__":
    main()