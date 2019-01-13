import os
import re
import csv
import talib
import msgpack
import numpy as np
inputs = {
    'open': np.random.random(100),
    'high': np.random.random(100),
    'low': np.random.random(100),
    'close': np.random.random(100),
    'volume': np.random.random(100)
}
#print (inputs)
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
            
            fileinput='indicators-'+key1+"-"+key2+".csv"
            fileoutput='indicators-'+key1+"-"+key2+".mpk"
            with open(fileoutput, 'wb') as outfile:
            
                with open(fileinput, newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    for row in spamreader:
                        columns=[]
                        for column in row:
                            columns.append(float(column))
                        msgpack.pack(columns, outfile)



            