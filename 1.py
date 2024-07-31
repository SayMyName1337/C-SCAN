# Creating a heatmap based on the data  which recorded in the .txt file

# Connecting a module for working with tabular data
import pandas as pd

# Connecting the Matplotlib library for data visualization
import matplotlib.pyplot as plt

# Connecting the Seaborn library for data visualization
import seaborn as sns

# Getting the file name
filename = 'C:\\Users\\SayMyName\\Desktop\\NIKIET\\data.txt'

# Reading data from a file into a table
df = pd.read_csv(filename, sep='\t', header=None)

# Table header output (first 5 rows in dataset)
df.head()

# Table size output
df.shape

# Printing the sum of missing values ​​for each column in a set
df.isna().sum()

# Printing the sum of missing values ​​across all columns in a dataset
df.isna().sum().sum()

# Removing the last column
df = df.iloc[:, :-1]

# Replacing a comma with a dot in all table cells and converting data to float
df = df.apply(lambda x: x.str.replace(',', '.').astype(float), axis=1)

# Output the table header
df.head()

# Construction of a correlation matrix with Pearson's coefficient
matr_corr = df.astype('float64').corr(method='pearson')

# Creating a new figure with the personal size
plt.figure(figsize = (10, 5))

# Heat map visualization for correlation matrix
sns.heatmap(df.corr(), annot = False, square = True, vmin = 0.0, cmap = "jet")

plt.title("C-SCAN",fontsize=12)

# Saving the result in png format in the current directory
plt.savefig("C-scan.png")

#plt.grid()  #You can put a grid if it needed
plt.show()