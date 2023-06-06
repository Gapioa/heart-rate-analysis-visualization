import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv(r'C:\Your_path_to_file.csv')

# Converting column 'Time' to String 
df['Time'] = df['Time'].astype(str)

# Selecting first 50 rows of data
df_first_50 = df.head(50)

# Creating the figure
fig = plt.figure(figsize=(10, 10))

# Graph 1 - Heart Rate Signal
ax1 = fig.add_subplot(3, 2, (1, 2))

#  Color the time with the sign "-" green
for i, row in df_first_50.iterrows():
    if '-' in row['Time']:
        ax1.plot(row['Time'], row['Heart rate (bpm)'], linestyle='None', marker='o', color='green')
    else:
        ax1.plot(row['Time'], row['Heart rate (bpm)'], linestyle='None', marker='o', color='blue')


ax1.set_ylim(50, 170)
#ax1.set_xlabel('Time')
ax1.set_ylabel('Heart rate (bpm)')
ax1.set_title('Heart Rate Signal')
ax1.tick_params(rotation=60, labelsize=8)  # Font change and rotation
ax1.grid(True)

#Graph 2 - Heart rate distribution histogram (Full Dataset)
ax2 = fig.add_subplot(3, 2, 3)
ax2.hist(df['Heart rate (bpm)'], bins=10, edgecolor='black')
ax2.set_xlabel('Heart rate (bpm)')
ax2.set_ylabel('Number of readings')
ax2.set_title('Distribution of heart values (Full Dataset)')

# Graph 3 - Cumulative histogram (entire base)
ax3 = fig.add_subplot(3, 2, 4)
ax3.hist(df['Heart rate (bpm)'], bins=10, cumulative=True, histtype='bar', edgecolor='black')
ax3.set_xlabel('Heart rate (bpm)')
ax3.set_ylabel('Cumulative frequency')
ax3.set_title('Cumulative Histogram (Full Dataset)')

# Calculation of basic statistical parameters (entire database)
mean = np.mean(df['Heart rate (bpm)'])
std = np.std(df['Heart rate (bpm)'])
kurtosis = df['Heart rate (bpm)'].kurtosis()
skewness = df['Heart rate (bpm)'].skew()
median = np.median(df['Heart rate (bpm)'])

# Graph 4 - Display of basic statistical parameters
ax4 = fig.add_subplot(3, 2, (5, 6))
ax4.axis('off')
ax4.text(0.1, 0.5, f"Mean: {mean}\nStandardna devijacija: {std}\nKurtosis: {kurtosis}\nSkewness: {skewness}\nMedijana: {median}",
         fontsize=12)

# Display graphs
plt.tight_layout()
plt.subplots_adjust(hspace=1)  # Change the spacing between subplots
plt.show()
