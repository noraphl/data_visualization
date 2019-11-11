#Pattern structure: attribute comparison_operator value AND attribute comparison_operator value AND ...
#The pattern must have the structure (spaces and capital letters for the operators)
#This program works for patterns with 4 numerical items in a binary classification
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
import matplotlib.lines as mlines
import pandas as pd
import seaborn as sns
import math  
import operator  

#Define dictionary for comparison operators
operator_dict={"<":operator.lt, "<=": operator.le, "=": operator.eq, "!=": operator.ne,">=": operator.ge, ">": operator.gt}
sns.set(style="darkgrid")
#Read data from csv file
data = pd.read_csv('https://raw.githubusercontent.com/noraphl/data_visualization/master/dataRank42.csv')

#Pattern
pattern_str = "funding_mean_2018 > 113.40 AND cites_per_auth_2015 > 18.96 AND doctype_confer_2016 > 528.50 AND art_per_auth_stdv_speed <= 36.07"
class_column = "class" 

items = pattern_str.split(' AND ')

att_val=[]

num_items = len(items)

for i in range(num_items):
    item = items[i].split(' ')
    att_val.append(item)

n1 = att_val[0][0]
n2 = att_val[1][0]
n3 = att_val[2][0]
n4 = att_val[3][0]
#Define data for axes x and y (first and second attribute)
x = data[n1]
y = data[n2]

#Define data that control size of markers (third attribute)
s = data[n3]

#Define data that control color of markers
c = data[n4]

#Get classes
ec = data[class_column]
uniq = list(set(ec))
uniq.sort()


#Set the colormap for fourth attribute
fc = plt.get_cmap('Greens')
cNormFc  = colors.Normalize(vmin=min(c), vmax=max(c))
scalarMapFc = cmx.ScalarMappable(norm=cNormFc, cmap=fc)

#Set the colormap for classes
cm = plt.get_cmap('hsv')
cNorm  = colors.Normalize(vmin=0, vmax=len(uniq))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)

pattern = False
fig, ax = plt.subplots()

for i in range(len(x)):
    #Assign a number according to the class
    if ec[i] == uniq[0]:
        edge = 0
    else:
        edge = 1
    fcolor = c[i]
   
    #Verify if data satisfies the pattern 
    if operator_dict[att_val[0][1]](x[i],float(att_val[0][2])) and operator_dict[att_val[1][1]](y[i],float(att_val[1][2])) and operator_dict[att_val[2][1]](s[i],float(att_val[2][2])) and operator_dict[att_val[3][1]](c[i],float(att_val[3][2])):
    #if data['funding_mean_2018'][i] > 113.40 and data['cites_per_auth_2015'][i] > 18.96 and data['doctype_confer_2016'][i] > 528.5 and data['art_per_auth_stdv_speed'][i] <= 36.07:
        pattern = True
    ax.scatter(x[i], y[i], s[i], c=[scalarMapFc.to_rgba(fcolor)],edgecolors=scalarMap.to_rgba(edge), marker='o', alpha=0.9)
    
    if pattern == True:
        ax.scatter(x[i], y[i], s[i]*.4, c='black', marker='x', alpha=1)
    
    pattern = False

#Plot labels
plt.xlabel(n1)
plt.ylabel(n2)

#Plot legend about class
class_a = mlines.Line2D([], [], color='w',markerfacecolor='w', markeredgecolor=scalarMap.to_rgba(0),marker='o',markersize=10, label=uniq[0])
class_b = mlines.Line2D([], [], color='w',markerfacecolor='w', markeredgecolor=scalarMap.to_rgba(1),marker='o',markersize=10, label=uniq[1])
legend1 = ax.legend(handles=[class_a, class_b],loc='upper left', facecolor='white',framealpha=0.8, title='Class')
ax.add_artist(legend1)

#Plot legend about path
pattern_mark = mlines.Line2D([], [], color='w',markerfacecolor='black',markeredgecolor='black', marker='x',markersize=10, label='Cover the pattern')
legend2=ax.legend(handles=[pattern_mark],loc='lower left', facecolor='white',framealpha=0.8, title='Pattern')
ax.add_artist(legend2)

#Plot legend about size
r1 = min(s)
r5 = max(s)
range_s = (r5-r1)/4
r2 = math.floor(r1 + range_s)
r3 = math.floor(r2 + range_s)
r4 = math.floor(r3 + range_s)
l1 = plt.scatter([],[], s=r1, edgecolors='none',color='gray',alpha=0.6)
l2 = plt.scatter([],[], s=r2, edgecolors='none',color='gray',alpha=0.6)
l3 = plt.scatter([],[], s=r3, edgecolors='none',color='gray',alpha=0.6)
l4 = plt.scatter([],[], s=r4, edgecolors='none',color='gray',alpha=0.6)
l5 = plt.scatter([],[], s=r5, edgecolors='none',color='gray',alpha=0.6)
labels = [str(r1), str(r2), str(r3), str(r4),str(r5)]
legend3 = plt.legend([l1, l2, l3, l4,l5], labels, loc = 1,facecolor='white',framealpha=0.8,  labelspacing=1,frameon=True,handletextpad=2,
title=n3, scatterpoints = 1)

#Plot colorbar
cbar = fig.colorbar(scalarMapFc)
cbar.ax.set_ylabel(n4, rotation=270,labelpad = 20)

plt.title("Pattern with 4 items \n" + pattern_str)

plt.show()