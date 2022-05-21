# importing of some useful libraries that will be used throughout the code.

import sys
import csv
import re
import os
import string
import random
import numpy as np
from functions import sort
from random import randrange
from datetime import timedelta

# In general, the datacreation file creates 3 artificial data sets: Patient, prescription and appointment schedule.


# 1 . Patients

# To start, it is important that a patient gets a free doctor as responsible. Free means here that he is still available (<500 patients). Hence, starting to read the health_pro csv file, the program then adds every doctor to a dictionary and gives him an inital count of 500. The rest follows later ...
with open('health_pro.csv') as f:
    dic_tmp2 = {}
    c = csv.reader(f, skipinitialspace=True, delimiter=',')
    for i in c:
        if i[2] != 'nurse' and i[2] != 'receptionist':
            s = i[0]
            dic_tmp2[s] = 0

# To create the patient data file, the for loop starts with a random choice of entries that should be created (500 or 1000 or 2500 or 5000). After this, the name, address and phone number of a patient will simply be created as a random string containing of two characters. After creating the personal data of the patient the dictionary created before will be used to give every patient an available doctor (If the count of 500 goes down to 0 then this doctor will be removed from the dictionary).
for i in range(0,random.choice([500,1000,2500,5000])):

    if dic_tmp2 == {}:
        break

    list1 = []

    # Note: The join function can be used for concatenation of two characters.    

    name = ''.join(random.choice(string.ascii_lowercase + '_')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(name)
    address = ''.join(random.choice(string.ascii_lowercase + '_')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(address)
    phone = ''.join(random.choice(string.ascii_lowercase + ' ')) + (random.choice(string.ascii_lowercase + ' '))
    list1.append(phone)
    employ_number = random.choice(list(dic_tmp2.keys()))
    list1.append(employ_number)
    a = ''
    for k,v in dic_tmp2.items():
        if k == employ_number:
            v = v+1
            dic_tmp2[k] = v
            if dic_tmp2[k] == 500:
                a = k
                break
    if a != '':
        dic_tmp2.pop(a)
            
    # For exporting the data, the loop still has to pay attention to start in writing the file (name is given through the command line, 1. argument). If so, then the "w" modus will be called. Otherwise, the append modus has to be chosen ("a"). 

    if i == 0:
        with open(sys.argv[1] + '.csv', 'w', newline='') as output:
                writer = csv.writer(output, delimiter = ",")
                writer.writerow(list1)
    else:
        with open(sys.argv[1] + '.csv', 'a', newline='') as output:
                writer = csv.writer(output, delimiter = ",")
                writer.writerow(list1)

# Finally, the just created patient csv will be read into a list_tmp so that it can be used for the appointment schedule csv file.
with open(sys.argv[1] + '.csv') as f:
    list_tmp = []
    c = csv.reader(f, skipinitialspace=True, delimiter=',')
    for i in c:
        list_patient = []
        list_patient.append(i[0])
        list_patient.append(i[1])
        list_patient.append(i[2])
        list_patient.append(i[3])
        list_tmp.append(list_patient)

# 2. APPOINTMENT SCHEDULE

# This function will be used to return a random date between two period of times (Here d1 = 01/01/2021 and d2 = 01/01/2022) whereas the correct time steps are also incorporated (see the list of seconds which represent always a correct time for the schedule) 
def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    int_delta = (random.randint(0, 365) * 24 * 60 * 60) + random.choice([28800,30600,32400,34200,36000,37800,39600,41400,43200,45000,50400,52200,54000,55800,57600,59400,61200,63000,64800])
    # int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    randomDate = randrange(int_delta)
    return start + timedelta(seconds=int_delta)

from datetime import datetime

d1 = datetime.strptime('1/1/2021 00:00:00.000', '%m/%d/%Y %H:%M:%S.%f')
d2 = datetime.strptime('1/1/2022 00:00:00.000', '%m/%d/%Y %H:%M:%S.%f')


list2 = []

# The process is similar to the patient file, once again a random number of entries will be used (500 or 1000 or 2500 or 5000)
for i in range(0,random.choice([500,1000,2500,5000])):
    list1 = []

    # random_date function created before will be used to give an appointment an almost random chance (within some restrictions to time and date)
    date = random_date(d1, d2)
    list1.append(date)
    # an almost random patient will be added (still a patient that is in the list_tmp, which is the patient file created before). Given one patient, all the necessary information are already gathered (personal data + doctor).
    patient = list_tmp[random.randint(0, len(list_tmp)-1)]
    employ_number = patient[3]
    list1.append(employ_number)
    p_name = patient[0]
    list1.append(p_name)
    p_address = patient[1]
    list1.append(p_address)
    p_phone = patient[2]
    list1.append(p_phone)

    list2.append(list1)

list2 = sort(list2,0,1)            
    # For exporting the data, the loop still has to pay attention to start in writing the file (name is given through the command line, 2. argument). If so, then the "w" modus will be called. Otherwise, the append modus has to be chosen ("a").

for i in range(0,len(list2)):
    if i == 0:
        with open(sys.argv[2] + '.csv', 'w', newline='') as output:
                writer = csv.writer(output, delimiter = ",")
                writer.writerow(list2[i])
    else:
        with open(sys.argv[2] + '.csv', 'a', newline='') as output:
                writer = csv.writer(output, delimiter = ",")
                writer.writerow(list2[i])

# 3. Precription

# Compared to the creations before, the prescirption file only contains of 10 or 50 or 100 prescriptions
# The rest of the data creation is similar to the two seen before.
list3 = []
for i in range(0,random.choice([10,50,100])):
    list1 = []   

    kind = random.choice(['aspegic 500','ibuprofen','immodium akut','aspegic 1000','prednisolon'])
    list1.append(kind)
    patient = list_tmp[random.randint(0, len(list_tmp)-1)]
    p_name = patient[0]
    list1.append(p_name)
    p_address = patient[1]
    list1.append(p_address)
    p_phone = patient[2]
    list1.append(p_phone)
    employ_number = patient[3]
    list1.append(employ_number)
    employ_number = patient[3]
    list1.append(employ_number)
    quantity = random.randint(0, 5)
    list1.append(quantity)
    dosage = random.uniform(0.00, 0.25)
    list1.append(dosage)

    list3.append(list1)

list3 = sort(list3,1,4)            
    # For exporting the data, the loop still has to pay attention to start in writing the file. If so, then the "w" modus will be called. Otherwise, the append modus has to be chosen ("a").

for i in range(0,len(list3)):
    if i == 0:
        with open(sys.argv[3] + '.csv', 'w', newline='') as output:
                writer = csv.writer(output, delimiter = ",")
                writer.writerow(list3[i])
    else:
        with open(sys.argv[3] + '.csv', 'a', newline='') as output:
                writer = csv.writer(output, delimiter = ",")
                writer.writerow(list3[i])