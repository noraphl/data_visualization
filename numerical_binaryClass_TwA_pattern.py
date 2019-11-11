#Pattern structure: attribute comparison_operator value AND attribute comparison_operator value AND ...
#The pattern must have the structure (spaces and capital letters for the operators)
#This program works for patterns with 2 numerical items in a binary classification
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
import matplotlib.lines as mlines
import pandas as pd
import seaborn as sns    
import operator

#Define dictionary for comparison operators
operator_dict={"<":operator.lt, "<=": operator.le, "=": operator.eq, "!=": operator.ne,">=": operator.ge, ">": operator.gt}
sns.set(style="darkgrid")
#Read data from csv file
data = pd.read_csv('https://raw.githubusercontent.com/noraphl/data_visualization/master/dataRank42.csv')

pattern_str = "cites_per_auth_2018 > 4.18 AND funding_mean_2017 > 86.88"
class_column = "class" 

items = pattern_str.split(' AND ')

att_val=[]

num_items = len(items)

for i in range(num_items):
    item = items[i].split(' ')
    att_val.append(item)

n1 = att_val[0][0]
n2 = att_val[1][0]


#Define data for axes x and y (first and second attribute)
x = data[n1]
y = data[n2]


#Get classes
ec = data[class_column]
uniq = list(set(ec))
uniq.sort()


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
   
    #Verify if data satisfies the pattern 
    if operator_dict[att_val[0][1]](x[i],float(att_val[0][2])) and operator_dict[att_val[1][1]](y[i],float(att_val[1][2])):
        pattern = True
    ax.scatter(x[i], y[i],s=90, c='orange',edgecolors=scalarMap.to_rgba(edge), marker='o', alpha=0.9)
    
    if pattern == True:
        ax.scatter(x[i], y[i],s=60, c='black', marker='x', alpha=1)
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
legend2=ax.legend(handles=[pattern_mark],loc='upper right', facecolor='white',framealpha=0.8, title='Pattern')
ax.add_artist(legend2)

plt.title("Pattern with 2 items \n" + pattern_str)
plt.show()