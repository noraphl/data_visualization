#Pattern structure: attribute comparison_operator value AND attribute comparison_operator value AND ...
#The pattern must have the structure (spaces and capital letters for the operators)
#This program works for patterns with 1 numerical item in a binary classification
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import operator

#Define dictionary for comparison operators
operator_dict={"<":operator.lt, "<=": operator.le, "=": operator.eq, "!=": operator.ne,">=": operator.ge, ">": operator.gt}
sns.set(style="darkgrid")

#Read data from csv file
data = pd.read_csv('https://raw.githubusercontent.com/noraphl/data_visualization/master/dataRank42.csv')

#Pattern
pattern_str = "cites_2017 > 71429.50"
class_column = "class" 

#Separate items
items = pattern_str.split(' AND ')

att_val=[]

num_items = len(items)

for i in range(num_items):
    item = items[i].split(' ')
    att_val.append(item)

n1 = att_val[0][0]

#Create a new column to indicate if the instance covers the pattern
y = data[n1]
c = np.empty(len(y), dtype=object)
for i in range(len(y)):
    if y[i] > float(att_val[0][2]):
        c[i]= 'Pattern'
    else:
        c[i] = 'No pattern'  

patt = pd.Series(c)
data['Pattern'] = patt

fig, ax = plt.subplots()  
sns.boxplot(x=class_column, y=n1, data=data, ax=ax,palette="vlag")  
sns.swarmplot(x=class_column, y=n1, hue='Pattern', data=data,size=2, palette='husl', linewidth=0)
plt.title("Pattern with 1 item \n" + pattern_str)
plt.show() 