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
            listInterval =[]
            with open(filename, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                lot=0
                maxRow=20
                listRow = []
                
                for row in spamreader:
                    if(lot>maxRow):
                        timeMin=0
                        timeMax=0
                        interval=0
                        for rowListmim in listRow:
                             for rowListmax in listRow:
                                if float(rowListmax[2])-float(rowListmim[2])>interval:
                                    timeMin=rowListmim[0]
                                    timeMax=rowListmax[0]
                                    interval=float(rowListmax[2])-float(rowListmim[2])
                                    listInterval.append({interval:interval,timeMin:timeMin,timeMax:timeMax})
                                
                        lot=lot=lot-1
                    else:
                        listRow.append(row)
                        lot=lot+1
            filecsv='interval-'+key1+"-"+key2+".csv"
            with open(filecsv, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in listInterval:
                    spamwriter.writerow([row['interval'],row['timeMin'],row['timeMax']])
            print('write '+filecsv)

