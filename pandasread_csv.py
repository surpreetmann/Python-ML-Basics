import numpy as np
import pandas as pd
import io
from google.colab import files
uploaded=files.upload()

#train_data=pd.read_csv(io.StringIO(uploaded['Salary_Data.csv'].decode('utf-8')))

#to read the data from csv file
train_data=pd.read_csv('Salary_Data.csv')
print('train data shape:',train_data.shape)

#to print the head of data
train_data.head()

#setting a value for column
train_data.minimum_nights='546'
print(train_data)

#to print the tail of data
train_data.tail()

#to print a particular columm
test=train_data[['Salary']]
print(test)

#to count number of rows in the data
train_data.count()

#to find minimum value of a column
train_data.Salary.min()

#group by mean
train_data.groupby('Salary').mean()[p]

#sort the values
train_data.sort_values(by=['','Minimum_Age']).reset_index(drop=True)[0:30]