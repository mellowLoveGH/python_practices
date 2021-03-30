import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re as re

def readData(path):
    data = pd.read_csv(path, header=0, error_bad_lines=False, index_col=False, dtype='unicode')
    return data;

def getColNames(csvdata):
    colnames = list(csvdata)
    return colnames;

def getColCount(colnames, csvdata):
    colfrequency = []
    for i in colnames:
        print(i)
        colfrequency.append(csvdata[i].count())
    return colfrequency;

def plotBar(colnames, colfrequency):
    df = pd.DataFrame({'name':colnames, 'frequncy':colfrequency})
    df.set_index("name",drop=True,inplace=True)
    df.plot.bar()
    plt.show()
    return;

def groupByDay(csvdata):
    csvdata.groupby('day').size().plot(kind='bar')
    plt.show()
    return;

def groupByTime(csvdata):
    times = pd.DatetimeIndex(csvdata['time'])
    csvdata.groupby([times.hour]).size().plot(kind='bar')
    plt.show()
    return;



path1='test_data/test_transaction_round2.csv'
path2='test_data/test_operation_round2.csv'

#full_data=[train, test]
#print(train.info())
#print(train.iloc[:,0].size)

'''
transaction=readData(path1)
tr_coln = getColNames(transaction)
tr_colf = getColCount(tr_coln, transaction)
plotBar(tr_coln, tr_colf)

operation=readData(path2)
op_coln = getColNames(operation)
op_colf = getColCount(op_coln, operation)
plotBar(op_coln, op_colf)

'''
transaction=readData(path1)
#groupByDay(transaction)
groupByTime(transaction)



























