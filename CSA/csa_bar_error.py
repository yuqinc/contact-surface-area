from pylab import *
from matplotlib import rc, rcParams 
import matplotlib.pyplot as plt
import numpy as np

def set_pub():
    rc('font', weight='bold')    # bold fonts are easier to see
    rc('ytick', labelsize=15)     # tick labels bigger
    rc('xtick', labelsize=15)
    #rc('lines', lw=1, color='k') # thicker black lines (no budget for color!)
    #rc('grid', c='0.5', ls='-', lw=0.5)  # solid gray grid lines
    rc('savefig', dpi=300)       # higher res outputs

set_pub()
###############Minor groove
axes =figure().add_subplot(111)
n_groups =3

#lys=(507,589,425)
#lys_std=(50,83,89)
#ack=(553,419,304)
#ack_std=(39,94,61)

lys=(569,685,540)
lys_std=(52,91,101)
ack=(677,460,405)
ack_std=(41,98,61)

lys_text = str(lys[1]) + u"\u00B1" + str(lys_std[1])

index = np.arange(n_groups)
bar_width = 0.15

opacity = 0.4
error_config = {'ecolor': '0.3'}

fig,ax=plt.subplots()
rects1 = plt.bar(index,lys, bar_width,
                  
                 color='r',
                 yerr=lys_std,
                 error_kw=error_config,
                 label='lys')
 
rects2 = plt.bar(index + bar_width, ack, bar_width,
                  
                 color='b',
                 yerr=ack_std,
                 error_kw=error_config,
                 label='ack')
 
for i in np.arange(3): 
    ax.text(index[i]-0.3, lys[i]+ lys_std[i]+10,'%s' % str(lys[i]) + u"\u00B1" + str(lys_std[i]))
    ax.text(index[i]+bar_width, ack[i]+ ack_std[i]+10,'%s' % str(ack[i]) + u"\u00B1" + str(ack_std[i]))

axis([-0.5,3,0,900]) 

plt.ylabel('Contact Surface Area ' r'$(\AA)^2 $',fontsize=16, weight= 'bold')
plt.xticks(index + 2*bar_width, ('lesion-free', 'trans-B[a]P', 'cis-B[a]P'))

plt.legend(loc='center right',numpoints=1, bbox_to_anchor=(1,1),fancybox=True, shadow=True, ncol=2)

#plt.tight_layout()
#plt.show()

savefig('csa_bar_with_error430-460.jpg',figsize=(8, 6), dpi=300, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None)
 
