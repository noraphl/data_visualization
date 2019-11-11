#Pattern structure: attribute comparison_operator value AND attribute comparison_operator value AND ...
#The pattern must have the structure (spaces and capital letters for the operators), string values must be with ('') 'value'
#Comparison operators: <, <=, =, !=, >, >=
#This program only works for patterns with 3 numerical items and 3 categorical items in a multiclass classification
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
import matplotlib.lines as mlines
import pandas as pd
import seaborn as sns
import math
import operator

def is_number(elem):
    try:
        float(elem)
        return True
    except ValueError:
        return False
#Define dictionary for comparison operators
operator_dict={"<":operator.lt, "<=": operator.le, "=": operator.eq, "!=": operator.ne,">=": operator.ge, ">": operator.gt}
sns.set(style="darkgrid")

#Read data from csv file
data = pd.read_csv('https://raw.githubusercontent.com/noraphl/data_visualization/master/automobile_price.csv')

#Pattern
pattern_str="wheel.base <= 98.95 AND make != 'nissan' AND engine.size <= 109.00 AND length <= 165.45 AND fuel.system != 'spdi' AND body.style != 'hardtop'"
#pattern_str = "city.mpg > 29.00 AND highway.mpg > 28.50 AND length <= 167.40 AND fuel.system != 'idi' AND body.style != 'hardtop' AND make != 'nissan'"
class_column = "price" 

items = pattern_str.split(' AND ')
att_val_cat=[]
att_val_num=[]

num_items = len(items)

for i in range(num_items):
    item = items[i].split(' ')
    if is_number(item[len(item)-1]):
        att_val_num.append(item)
    else:
        item[2] = item[2].replace("'","")
        att_val_cat.append(item)

if  len(att_val_num) == 3 and len(att_val_cat) == 3:
    n1 = att_val_num[0][0]
    n2 = att_val_num[1][0]
    n3 = att_val_num[2][0]
    
    c1 = att_val_cat[0][0]
    c2 = att_val_cat[1][0]
    c3 = att_val_cat[2][0] 

    #Define data for axes x and y, extract data for each attribute
    x = data[n1]
    y = data[n2]
    s = data[n3]
    p = data[c1]
    ec = data[c2]
    fc = data[c3]
    cl = data[class_column]

    #Obtain categories for edgecolor
    cat_ec = list(set(ec))
    cat_ec.sort()
    
    #Obtain categories point
    cat_p = list(set(p))
    cat_p.sort()
    
    #Obtain categories facecolor
    cat_fc = list(set(fc))
    cat_fc.sort()
    
    #Obtain classes
    class_data = list(set(cl))
    class_data.sort()
    
    #Set the colormap for edgecolor
    cme = plt.get_cmap('gist_rainbow')
    cNormCme  = colors.Normalize(vmin=0, vmax=len(cat_ec)-1)
    scalarMapE = cmx.ScalarMappable(norm=cNormCme, cmap=cme)
    
    #Set the colormap for facecolor
    cmf = plt.get_cmap('gist_ncar')
    cNormF  = colors.Normalize(vmin=0, vmax=len(cat_fc)-1)
    scalarMapF = cmx.ScalarMappable(norm=cNormF, cmap=cmf)
    
    #Set the colormap for point
    cmp = plt.get_cmap('nipy_spectral')
    cNormCmp  = colors.Normalize(vmin=0, vmax=len(cat_p)-1)
    scalarMapP = cmx.ScalarMappable(norm=cNormCmp, cmap=cmp)
    
    #Define shape for class
    mrk_elem_bs = ['o','D','s','^','p','H','v','8','h','d','<','>']
    pattern = False
    fig, ax = plt.subplots()

    for i in range(len(x)):
        #Determine values for facecolor, edgecolor, class, point
        for j in range (len(cat_fc)):
            if fc[i] == cat_fc[j]:
                fcolor = j
                break;
        for j in range (len(cat_ec)):
            if ec[i] == cat_ec[j]:
                edge = j
                break;
            
        for j in range (len(class_data)):
            if cl[i] == class_data[j]:
                mkr = mrk_elem_bs[j] 
                break;
    
        for j in range (len(cat_p)):
            if p[i] == cat_p[j]:
                star_color = j
                break;
        
        #Verify if data satisfies the pattern 
        if operator_dict[att_val_num[0][1]](x[i],float(att_val_num[0][2])) and operator_dict[att_val_num[1][1]](y[i],float(att_val_num[1][2])) and operator_dict[att_val_num[2][1]](s[i],float(att_val_num[2][2])) and operator_dict[att_val_cat[0][1]](p[i],att_val_cat[0][2]) and operator_dict[att_val_cat[1][1]](ec[i],att_val_cat[1][2]) and operator_dict[att_val_cat[2][1]](fc[i],att_val_cat[2][2]):
            pattern = True
            
        #Plot data
        ax.scatter(x[i], y[i],s[i], c=[scalarMapF.to_rgba(fcolor)],edgecolors=scalarMapE.to_rgba(edge),linewidth='1.4', marker=mkr, alpha=0.7)
        ax.scatter(x[i], y[i], s[i]*.7, c=[scalarMapP.to_rgba(star_color)], marker='.', alpha=0.9)
        
        #Plot pattern
        if pattern == True:
            ax.scatter(x[i], y[i], s[i]*0.4, c='black', marker='x', alpha=1)
    
        pattern = False

    #Plot labels
    plt.xlabel(n1)
    plt.ylabel(n2)
    
    #Plot legends
    fc_label = []
    for x in range (len(cat_fc)):
        fc_label.append(mlines.Line2D([], [], color='w',markerfacecolor=scalarMapF.to_rgba(x),marker='o',markersize=10, label=cat_fc[x]))
    legend1 = ax.legend(handles=fc_label,loc='upper left', facecolor='white',framealpha=0.8, title=c3,fontsize=7 )
    ax.add_artist(legend1)

    p_label = []
    for x in range(len(cat_p)):
        p_label.append(mlines.Line2D([], [], color='w',markerfacecolor=scalarMapP.to_rgba(x),marker='.',markersize=10, label=cat_p[x]))
    legend2 = ax.legend(handles=p_label,loc='upper center', facecolor='white',framealpha=0.8, title=c1,fontsize=7 )
    ax.add_artist(legend2)

    ec_label = []
    for x in range(len(cat_ec)):
        ec_label.append(mlines.Line2D([], [], color='w',markerfacecolor='w',markeredgecolor=scalarMapE.to_rgba(x),marker='o',markersize=10, label=cat_ec[x]))
    legend3 = ax.legend(handles=ec_label,loc='lower center', facecolor='white',framealpha=0.8, title=c2,fontsize=9 )
    ax.add_artist(legend3)

    class_label = []
    for x in range(len(class_data)):
        class_label.append(mlines.Line2D([], [], color='w', markerfacecolor='w', markeredgecolor='black',marker=mrk_elem_bs[x],markersize=10, label=class_data[x]))
    legend5 = ax.legend(handles=class_label,loc='upper right', facecolor='white',framealpha=0.8, title='Class',fontsize=9 )
    ax.add_artist(legend5)

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
    legend6 = ax.legend([l1, l2, l3, l4,l5], labels, loc ='lower right',facecolor='white',framealpha=0.8,  labelspacing=1,frameon=True,
                        title=n3, scatterpoints = 1, )
    ax.add_artist(legend6)

    #Plot legend about path
    pattern_mark = mlines.Line2D([], [], color='w',markerfacecolor='black',markeredgecolor='black', marker='x',markersize=7, label='Cover the pattern')
    legend4=ax.legend(handles=[pattern_mark],loc='lower left', facecolor='white',framealpha=0.7, title='Pattern', fontsize=7)
    ax.add_artist(legend4)

    plt.suptitle("Pattern with 3 numerical items and 3 categorical items, multiclass classification \n'" + pattern_str)

    plt.show()