from pylab import *
from matplotlib import rc, rcParams 
import matplotlib.pyplot as plt

def set_pub():
    rc('font', weight='bold')    # bold fonts are easier to see
    rc('ytick', labelsize=20)     # tick labels bigger
    rc('xtick', labelsize=20)
    #rc('lines', lw=1, color='k') # thicker black lines (no budget for color!)
    #rc('grid', c='0.5', ls='-', lw=0.5)  # solid gray grid lines
    rcParams['figure.figsize']=12,5
    rc('savefig', dpi=300)       # higher res outputs

set_pub()
###############Minor groove
fig,ax=plt.subplots()

index = range(8)
dataMatrix =genfromtxt('minor.out')
 
errorbar(index, dataMatrix[:,0],dataMatrix[:,1],label =r'R-cdG', c ='red', marker="^", markersize =10, linewidth=2.0)
errorbar(index, dataMatrix[:,2],dataMatrix[:,3],label =r'S-cdG', c ='blue', marker="^", markersize =10, linewidth=2.0)
errorbar(index, dataMatrix[:,4],dataMatrix[:,5],label =r'Unmod-dG', c ='green', marker="^", markersize =10,linewidth=2.0)
errorbar(index, dataMatrix[:,6], dataMatrix[:,7],label =r'cis-B[a]P-dG', c ='black', marker="^", markersize =10, linewidth=2.0)

#legend(loc = 'center',numpoints=1, ncol=2,borderaxespad=0.25, bbox_to_anchor=[0.5,0.9])

#xlabel('Step', fontsize =16, weight= 'bold')
plt.ylabel('Minor groove width ' r'$(\AA)$',fontsize=20, weight= 'bold')
plt.axis([-1, 8, 2, 12])
 
a=ax.get_xticks().tolist()
a=['']
for i in range(8):
    a.append("P"+str(70+i)+"-"+"P"+str(225-i))
#a = ['','P70-P225', 'P71-P224', 'P72-P223','P73-P222','P74-P221','P75-P220','P76-P219','P77-P218']
 
ax.set_xticklabels(a,rotation= 22,rotation_mode="anchor",fontsize =20, weight='bold')
plt.margins(0.8)

#show()
savefig('minor_groove_block_error_june16_nolegend.jpg', facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None)
 
