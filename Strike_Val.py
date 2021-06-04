import sys
import numpy as np
DATE_COL = 9
SV_COL = 11
STRIKE_COL = 0
VALUE_COL = 1
LINE_COL = 7

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
        splitter = line.split('|')
        if splitter[LINE_COL] == "1":
            continue
        if splitter[DATE_COL] == month + "/" + year:
            if len(combineArr) == 0:
                #strikeArr = splitter[SV_COL].split(':')
                #combineArr = strikeArr
                combineArr = splitter[SV_COL].split(':')
            else:
                tempArr = splitter[SV_COL].split(':')
                combineArr += tempArr
                #combineArr = np.concatenate(strikeArr, tempArr)
    filer.close()
    return combineArr

def format_output(data):
    count = 1
    checker = ""
    for x in data:
        arr = x.split('/')
        value = arr[VALUE_COL]
        checker = arr[VALUE_COL]
        if value.endswith("#"):
            checker = value.rstrip(value[-1])
        print("Strike" + " = " + arr[STRIKE_COL] + "\tValue" + " = " + checker)
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