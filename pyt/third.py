import os
import re
import csv
for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)
        if filename.startswith( 'eggs' ) & filename.endswith('.csv'):
            m = re.search('eggs(?P<key1>\w+)-(?P<key2>\w+).csv', filename)
            if m is None:
                continue
            key1= None
            key2= None
            if m is not None:
                key1=m.group('key1')
                key2=m.group('key2')
            print('key1'+key1)
            print('key2'+key2)
            print(filename)
            filecsv='interval-'+key1+"-"+key2+".csv"
            listLong = []
            listShort = []
            with open(filecsv, newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    for row in spamreader:
                        listLong.append(row[1])
                        listShort.append(row[2])
                        if len(listLong) >100 :
                            listLong.pop(0)
                            listShort.pop(0)
                    listLong=set(listLong)
                    listShort=set(listShort)

            with open(filename, newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    for row in spamreader:



