# Russia Tile Grid Map
# Плиточная карта России
# 4 типа и 4 цвета

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

grid_table = pd.read_csv('./grid_table.csv', sep = ";")
n = grid_table.shape[0]

# colors
c1 = '#E0EEEE'
c2 = '#ff0000'
c3 = '#ffff00'
c4 = '#ffbf00'

# types
types = pd.DataFrame(data = {'type':[1,2,3,4], 'color':[c1,c2,c3,c4]})

# for legend
t1 = patches.Patch(color = c1, label = 'тип 1')
t2 = patches.Patch(color = c2, label = 'тип 2')
t3 = patches.Patch(color = c3, label = 'тип 3')
t4 = patches.Patch(color = c4, label = 'тип 4')

# make data
random_type = np.random.choice([1,2,3,4], size = n, replace = True) # random state to join color
grid_table['type'] = random_type
grid_table = grid_table.merge(types, how = 'left', on = 'type')

nrow = 19
ncol = 11

fig, axs = plt.subplots(1, figsize=(10, 5), dpi=300)
plt.xlim(0, 19)
plt.ylim(0, 12)
plt.axis('off')
axs.set_aspect('equal')
for _, state in grid_table.iterrows():
    box = patches.Rectangle((state['col'], ncol - state['row']), 1, 1, 
                            linewidth=1, edgecolor='white',facecolor = state['color'])
    plt.text(state['col'] + 0.5, ncol - state['row'] + 0.5, 
             state['subj_rus'], 
             horizontalalignment='center', 
             verticalalignment='center', 
             color='black', weight='normal', fontsize = 'x-small')
    axs.add_patch(box)

plt.title('заголовок')
plt.legend(handles=[t1, t2, t3, t4], handlelength=0.7, 
           loc = 'lower center', fontsize = 'xx-small', frameon = False)
# plt.show()
plt.savefig('map.png', bbox_inches='tight', transparent=True)