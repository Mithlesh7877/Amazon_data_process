# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:06:30 2019

@author: My PC
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#dataset importing
ds=pd.read_csv(r"C:\Users\My PC\Desktop\Machine Learning\Amazon_orders\amazon-orders.csv")
ds.head()
ds.shape
New_Nandrop_data=ds.drop(['Purchase Order Number','Shipping Address Street 2','Group Name'],axis=1)
New_Nandrop_data["Total Charged"] = New_Nandrop_data["Total Charged"].str.replace('$','').astype(float)
New_Nandrop_data["Subtotal"] = New_Nandrop_data["Subtotal"].str.replace('$','').astype(float)
New_Nandrop_data["Shipping Charge"] = New_Nandrop_data["Shipping Charge"].str.replace('$','').astype(float)
New_Nandrop_data["Tax Before Promotions"] =New_Nandrop_data["Tax Before Promotions"].str.replace('$','').astype(float)
New_Nandrop_data["Total Promotions"] = New_Nandrop_data["Total Promotions"].str.replace('$','').astype(float)
New_Nandrop_data["Tax Charged"] = New_Nandrop_data["Tax Charged"].str.replace('$','').astype(float)
Total=New_Nandrop_data["Total Charged"].sum()
Min=New_Nandrop_data["Total Charged"].min()
Max=New_Nandrop_data["Total Charged"].max()
Tax_Total=New_Nandrop_data["Tax Charged"].sum()
New_Nandrop_data['Order Date'] = pd.to_datetime(New_Nandrop_data['Order Date'])
#New_Nandrop_data.plot.bar("Order Date","Total Charged",figsize=(20,10))
Daily_t_order=New_Nandrop_data.groupby("Order Date").sum()["Total Charged"]
#Daily_t_order.plot.bar(figsize=(20,10))
New_Nandrop_data['Month'] = New_Nandrop_data['Order Date'].dt.month  #Read about dt.month
Daily_Mt_order=New_Nandrop_data.groupby("Month").sum()["Total Charged"]
#Daily_Mt_order.plot.bar(figsize=(20,10))













