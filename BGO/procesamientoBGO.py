import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

archivo = 'OpticalPhotonCount.phsp'
data = pd.read_csv(archivo,sep=r"\s+",skiprows=0,usecols=[4, 5], header=None)

#[4] Tiempo de vuelo [ns]
#[5] ProcessID: 1 Scintillation, 2 Cerenkov, 3 Absorption

centelleo = data.loc[data[5] == 1, 4]
cherenkov = data.loc[data[5] == 2, 4]


plt.hist(centelleo, bins=50, label="Centelleo")
plt.hist(cherenkov, bins=50, label="Cherenkov")
plt.xlabel("Tiempo de vuelo [ns]")
plt.ylabel("Frecuencua [a.u.]")
plt.title('Comparativa Centelleo vs Cherenkov')
plt.yscale('log')
plt.legend()
plt.show()

