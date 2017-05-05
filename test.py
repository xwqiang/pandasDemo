#!/usr/bin/env python3
# !/usr/bin/python3
import pandas as pd
import numpy as np


def testwithhead():
    # sql = pd.read_table('/Users/xuwuqiang/Downloads/sql.info', sep='\t',
    #                     names=['ID', 'USER', 'HOST', 'PID', 'DB', 'COMMAND', 'TIME', 'STATE', 'INFO'])
    sql = pd.read_table('sql.info', sep='\t',
                        header=0)
    # print(sql.groupby(['HOST']).count())
    print(sql.head())
    # print(sql.index)
    # print(sql.columns)

def testnohead():
    sql = pd.read_table('sql-nohead.info', sep='\t',header=None,
                        names=['ID', 'USER', 'HOST', 'PID', 'DB', 'COMMAND', 'TIME', 'STATE', 'INFO'])
    print(sql.head())
    # print(sql.groupby(['HOST']).count())
    # print(sql.groupby(['HOST']).count().sort(['ID'],ascending=False))
    # print(sql.groupby(['HOST']).count().sort_values(by=['ID'],ascending=False)) #sort的另外一种写法
    print('----------------------')
    df = sql.groupby(['HOST']).count().sort_values(by=['ID'],ascending=False)
    print(df[0:1])
    print('----------------------')
    print(df[0:1]['ID'][0])
    # print(sql.index)
    # print(sql.columns)


if __name__ == '__main__':
    # testwithhead()
    testnohead()


def tt():
    df = pd.DataFrame(
        {'id': [1, 1, 3, 4], 'value': ['a1', 'a2', 'a3', 'a4'], 'type': [5, 6, 7, 7]},
        columns=['id', 'value', 'type'])

    print(df)
    print('-----------')
    print(df.groupby(['id']).count())
    print('-----------')
    print(df['id'])
    print('-----------')

    print(dir(df))
