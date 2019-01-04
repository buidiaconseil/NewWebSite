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
            try:
                os.remove(filecsv)
            except:
                print ('clean '+filecsv)
            listInterval =[]

            for maxRow in [20,60,300]:
                
                with open(filename, newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    lot=0
                    
                    listRow = []
                    
                    for row in spamreader:
                        if(lot>maxRow):
                            timeMin=0
                            timeMax=0
                            
                            for rowListmim in listRow:
                                interval=0
                                for rowListmax in listRow:
                                    newInterval=(float(rowListmax[2])-float(rowListmim[2]))/float(rowListmim[2])
                                    if newInterval>interval:
                                        timeMin=rowListmim[0]
                                        timeMax=rowListmax[0]
                                        interval=newInterval
                                        listInterval.append({'interval':interval,'timeMin':timeMin,'timeMax':timeMax,'window':maxRow})
                            listRow.pop(0)
                                    
                            lot=lot=lot-1
                        else:
                            listRow.append(row)
                            lot=lot+1
                finalList=[]
                setTime=set()
                for row in listInterval:
                    
                    timeref=row['timeMin']
                    if timeref in setTime:
                        continue
                    setTime.add(timeref)
                    best=row
                    for rowSec in listInterval:
                        if timeref==rowSec['timeMin'] and rowSec['interval']>row['interval']:
                            best=rowSec
                    finalList.append(best)
                finalList=sorted(finalList, key=lambda student: float(student['interval']))
                with open(filecsv, 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for row in finalList:
                        spamwriter.writerow([row['interval'],row['timeMin'],row['timeMax'],row['window']])
            print('write '+filecsv)

