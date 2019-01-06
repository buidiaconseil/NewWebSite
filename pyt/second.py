import os
import re
import csv
import time
for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)
        if filename.startswith( 'eggs' ) & filename.endswith('.csv'):
            startTime=time.time()*1000.0
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

            for maxRow in [200]:
                counterline=0
                with open(filename, newline='') as csvfile:
                   
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    lot=0
                    
                    listRow = []
                    listRowMax=[]
                    hashedCal={}
                    savedList=[]
                    for rowListmim in spamreader:
                        savedList.append(rowListmim)
                        #if counterline>1000:
                        #    break
                        #counterline=counterline+1
                        
                    readTime=time.time()*1000.0
                    print("read "+str(readTime-startTime))
                    for row in savedList:
                        listRow.append(row)
                        listRowMax.append(row)
                        timeMin=0
                        timeMax=0
                        if(lot>maxRow):
                            
                            
                            countpop=0
                            for rowListmim in listRow:
                                

                                interval=0
                                haschange=False
                                for rowListmax in listRowMax:
                                    
                                    key=rowListmim[0]+":"+rowListmax[0]
                                    listmin=float(rowListmim[2])
                                    newInterval=(float(rowListmax[2])-listmin)/listmin
                                    if newInterval>interval:
                                        timeMin=rowListmim[0]
                                        timeMax=rowListmax[0]
                                        interval=newInterval
                                        listInterval.append({'interval':interval,'timeMin':timeMin,'timeMax':timeMax,'window':maxRow})
                                countpop=countpop+1
                            listRow.pop(0)
                            listRowMax=[]
                            lot=lot-1
                        else:
                            lot=lot+1
                intervalTime=time.time()*1000.0
                print("interval "+str(intervalTime-startTime))
                finalList=[]
                setTime={}
                setTimeMax={}
                listInterval=sorted(listInterval, key=lambda student: float(student['timeMin']))
                sortTime=time.time()*1000.0
                print("sort "+str(sortTime-intervalTime))
                for row in listInterval:
                    
                    timeref=row['timeMin']
                    timeMaxRef=row['timeMax']
                    if timeref in setTime:
                        continue
                    if row['timeMax'] in setTimeMax:
                        continue 
                    setTime[timeref]=timeref
                    best=row
                    for rowSec in listInterval:
                        
                        if rowSec['timeMax'] in setTimeMax:
                            continue
                        if timeref==rowSec['timeMin'] and rowSec['interval']>row['interval']:
                            best=rowSec
                        if timeref!=rowSec['timeMin']:
                            break
                    setTimeMax[best['timeMax']]=best['timeMax']
                    finalList.append(best)
                
                sel1Time=time.time()*1000.0
                print("sel1Time "+str(sel1Time-sortTime))
                finalList=sorted(finalList, key=lambda student: float(student['interval']), reverse = True)
                sel1TimeBis=time.time()*1000.0
                print("sel1Timebis "+str(sel1TimeBis-sel1Time))
                newfinalList=[]
                for secorow in finalList:
                    existin=False
                    targetMin=float(secorow['timeMin'])
                    targetMax=float(secorow['timeMax'])
                    for minrow in newfinalList:
                        checkMin=float(minrow['timeMin'])
                        checkMax=float(minrow['timeMax'])
                        if (targetMin>checkMin and targetMin<checkMax) or  (targetMax>checkMin and targetMax<checkMax):
                                existin=True
                                continue
                        
                    if not existin:
                        newfinalList.append(secorow)
                sel2Time=time.time()*1000.0
                print("sel2Time "+str(sel2Time-sel1Time))
                newfinalList=sorted(newfinalList, key=lambda student: float(student['interval']))
                with open(filecsv, 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for row in newfinalList:
                        spamwriter.writerow([row['interval'],row['timeMin'],row['timeMax'],row['window']])
            print('write '+filecsv)

