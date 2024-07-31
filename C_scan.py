import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


'''
 A-SCAN data
arrays=[[[1.2, 2.5, 3.6], [5.1, 2.4, 7.2], [7.8, 2.2, 8.4]],
        [[2.4, 4.5, 5.1], [6.9, 3.4, 8.3], [1.6, 2.5, 3.6]],
        [[4.0, 2.9, 7.9], [7.8, 7.6, 4.4], [3.6, 2.7, 1.9]]]
random.shuffle(arrays)  Random redistribution of max values for performance testing
print("A-SCAN data: \n",arrays, "\n")
'''

# Creating a 3D array where
'''
The first number is the number of rows containing the arrays
The second is the number of arrays contained in the string
The third is the number of elements in each array
'''
np.set_printoptions(precision=1, floatmode='fixed')
arrays = np.random.uniform(0.0, 100.0, (50,100,3))
print("A-SCAN data: \n",arrays, "\n")


# Searching the max value to all massives and print them
maximums=list(map(lambda x: list(map(max,x)),arrays))

# Creating heatmap
sns.heatmap(maximums,annot=False,fmt='.1f',vmin=0.0, cmap = "jet")
plt.title("test C-scan with static data",fontsize=12)


plt.savefig("C-scan with static data.png")
plt.show()