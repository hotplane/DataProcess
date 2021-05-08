import numpy as np
import pandas as pd
import os
import tkinter as tk
import copy
from tkinter import filedialog



# def cut(old,start,end):
#     print(old[start:end])
#     tmp=old[start:end]
#     old=tmp
#     print(old)
    

#设置目录选择
# root = tk.Tk()
# root.withdraw()
# filepath = filedialog.askdirectory() 
# print(filepath)
filepath='D:\\Source Code\\py\\数据处理\\一次调频考核数据'
#遍历当前目录下面的文件
filename=os.listdir(filepath)
#print(filename[0])

####读取Excel表格
allfilenanme=filepath+'\\'+filename[0]
data=pd.read_excel(allfilenanme)
#print(data.columns)

#读取每一行
# linedata = data.ix[0].values

# #########################处理数据##################
# ###处理第一列数据，获得电厂名称
# linedate[0]=linedate[0][3:5]

# ###处理第二列数据，获得机组编号
# linedate[1]=linedate[1][12]


# print(linedate)

# # linedate[0]=linedate[0][3:5]
   

# # # type(linedate)
# # print(linedate[0])



# # linedate = data.ix[1].values
# # type(linedate)
# # print(linedate)