# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 01:31:40 2020

@author: Aashi
"""


import numpy as np
import pandas as pd
import xlsxwriter
import re
df = pd.read_csv(r'C:\Users\Aashi\Desktop\grofers_jio.csv') #dataframe


df.Quantity =df.Quantity.apply(lambda x: x.replace(' ','')) 



def min_price (Item,Quantity):
    l=list(filter(lambda x: Item in x.lower(),df.Item)) #lambda function to find the substring in the item
    #if (Item.isin(l))&&(Quantity==df.Quantity)
    df_j=df[(df.Website == 'JioMart')&(df.Item.isin(l))&(df.Quantity==Quantity)] #finding tem and quantity in jiomart
    df_g=df[(df.Website == 'Grofers')&(df.Item.isin(l))&(df.Quantity==Quantity)] #finding item and quantity in grofers
    df_f = df[((df.Website=='JioMart') | (df.Website == 'Grofers')) &(df.Item.isin(l))&(df.Quantity==Quantity)] #combining tems from jiomart and grofers
  
    df_j[df_j['Price']==df_j['Price'].min()][['Website','Item','Quantity','Price']] #finding min price in jiomart
    df_g[df_g['Price']==df_g['Price'].min()][['Website','Item','Quantity','Price']]#finding min price in grofers
       
    df_1 = pd.DataFrame(columns = ['Website','Item','Quantity','Price']) #headers for dataframe
    df_1 = df_1.append(df_j[df_j['Price']==df_j['Price'].min()][['Website','Item','Quantity','Price']]) #appending min price for jiomart
    df_1 = df_1.append(df_g[df_g['Price']==df_g['Price'].min()][['Website','Item','Quantity','Price']]) #appending min price for grofers
    return(df_1)

Item= input("Provide Item : ") #input for item
Quantity= input("Provide Quantity : ") #input for quantity
    
print('',min_price(Item,Quantity)) #calling function min_price
   