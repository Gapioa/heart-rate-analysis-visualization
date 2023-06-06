import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Učitavanje datoteke
df = pd.read_csv(r'C:\Users\kalma\Desktop\Fax\Treća godina\Treći trimestar\Informacioni sistemi u medicini\ISUM\Heart rate_Feb92023-May82023.csv')

# Konvertovanje kolone 'Time' u String tip podataka
df['Time'] = df['Time'].astype(str)

# Izdvajanje prvih 50 vrednosti iz baze
df_first_50 = df.head(50)

# Kreiranje Figure objekta
fig = plt.figure(figsize=(10, 10))

# Grafik 1 - Heart Rate Signal
ax1 = fig.add_subplot(3, 2, (1, 2))

# Oboji vreme sa znakom "-" u zeleno
for i, row in df_first_50.iterrows():
    if '-' in row['Time']:
        ax1.plot(row['Time'], row['Heart rate (bpm)'], linestyle='None', marker='o', color='green')
    else:
        ax1.plot(row['Time'], row['Heart rate (bpm)'], linestyle='None', marker='o', color='blue')


ax1.set_ylim(50, 170)
#ax1.set_xlabel('Time')
ax1.set_ylabel('Heart rate (bpm)')
ax1.set_title('Heart Rate Signal')
ax1.tick_params(rotation=60, labelsize=8)  # Promena fonta i rotacije
ax1.grid(True)

#Grafik 2 - Histogram raspodele srčanih vrednosti (cela baza)
ax2 = fig.add_subplot(3, 2, 3)
ax2.hist(df['Heart rate (bpm)'], bins=10, edgecolor='black')
ax2.set_xlabel('Srčani ritam (bpm)')
ax2.set_ylabel('Broj očitavanja')
ax2.set_title('Raspodela srčanih vrednosti (Full Dataset)')

# Grafik 3 - Kumulativni histogram (cela baza)
ax3 = fig.add_subplot(3, 2, 4)
ax3.hist(df['Heart rate (bpm)'], bins=10, cumulative=True, histtype='bar', edgecolor='black')
ax3.set_xlabel('Srčani ritam (bpm)')
ax3.set_ylabel('Kumulativna frekvencija')
ax3.set_title('Kumulativni histogram (Full Dataset)')

# Izračunavanje osnovnih statističkih parametara (cela baza)
prosek = np.mean(df['Heart rate (bpm)'])
std = np.std(df['Heart rate (bpm)'])
kurtosis = df['Heart rate (bpm)'].kurtosis()
skewness = df['Heart rate (bpm)'].skew()
medijana = np.median(df['Heart rate (bpm)'])

# Grafik 4 - Prikaz osnovnih statističkih parametara
ax4 = fig.add_subplot(3, 2, (5, 6))
ax4.axis('off')
ax4.text(0.1, 0.5, f"Prosek: {prosek}\nStandardna devijacija: {std}\nKurtosis: {kurtosis}\nSkewness: {skewness}\nMedijana: {medijana}",
         fontsize=12)

# Prikaz grafova
plt.tight_layout()
plt.subplots_adjust(hspace=1)  # Promena razmaka između podgrafika
plt.show()
