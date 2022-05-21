# importing of some useful libraries that wil be used throughout the code.

import csv
import sys
import re
import os
import string
import random
import operator

# load_csv
# it opens the file with "with", reads every line with "csv.reader" and uses then a for loop to get every value in one line which is seperated in the csv file by a "," and appends this to a temporary list. If every value in one line is read, then the temporary list (list_tmp) will be added to the main list called "list1" 

def load_csv(file,row_length):
    list1 = []
    with open(file) as f:
        c = csv.reader(f, skipinitialspace=True, delimiter=',')
        for i in c:
            list_tmp = []
            for j in range(0,row_length):
                list_tmp.append(i[j])
            list1.append(list_tmp)
    return list1

# write_csv
# the write_csv functiion takes a file name, a string which differentiates between adding new value or deleting existing values and an existing list as arguments and it writes either a new line to an existing csv file or it overwrites the entire file.

def write_csv(file,add_or_delete,list):
    # If "add" is the process to be done, then it only inserts a new line into the csv file (the last entry that has been appended to the list).  
    if add_or_delete == "add":
        with open(file, 'a', newline='') as output:
                writer = csv.writer(output, delimiter=",")
                writer.writerow(list[-1])
    # If "delete" has to be done, then it overwrites the csv file in choosing the writing modus "w" for the first entry of the list and the append modus "a" for all the following ones. 
    if add_or_delete == "delete":
        counter = 0
        for i in list:
            # the counter will be increased after the first insertion process so that it only goes once into this case. In all other cases it directly goes into "else". 
            if counter == 0:
                with open(file, 'w', newline='') as output:
                    writer = csv.writer(output, delimiter = ',')
                    # list_tmp is a temporary list which always changes for every line that will be inserted.
                    list_tmp = []
                    for j in i:
                        # because the patient data are still included into the list as a tuple, the function makes here the check whether the entry is a tuple. If so, then it also chooses every entry of this tuple as a single entry and appends it to the temporary list "list_tmp".
                        if type(j) is tuple:
                            for k in j:
                                list_tmp.append(k)
                        else:
                            list_tmp.append(j)
                    writer.writerow(list_tmp)
                    counter += 1
            # "else" is used for all insertion steps for the second up to the last entry in the list.
            else:
                with open(file, 'a', newline='') as output:
                    writer = csv.writer(output, delimiter=",")
                    list_tmp = []
                    for j in i:
                        if type(j) is tuple:
                            for k in j:
                                list_tmp.append(k)
                        else:
                            list_tmp.append(j)
                    writer.writerow(list_tmp)

# the sort function is used to bring more order into the csv file. Therefore it sorts a list by a first criteria and afterwards also by a second criteria. For this, it uses the sort built-in "sort" function which uses the Timsort algorithm which is a combination of insertion and merge sort.

def sort(list, item1, item2):
    list1 = sorted(list, key=operator.itemgetter(item1, item2))
    return list1